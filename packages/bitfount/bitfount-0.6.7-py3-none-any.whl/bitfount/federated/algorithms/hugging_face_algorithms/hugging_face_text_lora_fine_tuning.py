"""Hugging Face Text LoRA Fine Tuning Algorithm."""
from __future__ import annotations

import os
from pathlib import Path
import platform
from typing import TYPE_CHECKING, Any, ClassVar, Dict, List, Mapping, Optional, Union

from datasets import Dataset, DatasetDict
from marshmallow import fields
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    DataCollatorForLanguageModeling,
    Trainer,
    TrainingArguments,
)

from bitfount.config import BITFOUNT_OUTPUT_DIR
from bitfount.data.datasources.base_source import BaseSource
from bitfount.federated.algorithms.base import (
    BaseAlgorithmFactory,
    BaseModellerAlgorithm,
    BaseWorkerAlgorithm,
)
from bitfount.federated.logging import _get_federated_logger
from bitfount.types import T_FIELDS_DICT

if TYPE_CHECKING:
    from bitfount.federated.privacy.differential import DPPodConfig


DEFAULT_RETURN_WEIGHTS = False

DEFAULT_LORA_R = 8
DEFAULT_LORA_ALPHA = 8
DEFAULT_LORA_DROPOUT = 0.0
DEFAULT_LORA_BIAS = "none"
DEFAULT_TASK_TYPE = "CAUSAL_LM"

DEFAULT_PER_DEVICE_TRAIN_BATCH_SIZE = 8
DEFAULT_GRADIENT_ACCUMULATION_STEPS = 1
DEFAULT_WARMUP_STEPS = 0
DEFAULT_MAX_STEPS = -1
DEFAULT_LEARNING_RATE = 5e-5
DEFAULT_LOGGING_STEPS = 500
DEFAULT_OPTIMIZER = "adamw_hf"
DEFAULT_LR_SCHEDULER_TYPE = "linear"

logger = _get_federated_logger(__name__)


class _ModellerSide(BaseModellerAlgorithm):
    """Modeller side of the HuggingFaceTextLoraFineTuning algorithm."""

    def initialise(self, task_id: Optional[str] = None, **kwargs: Any) -> None:
        """Nothing to initialise here."""
        pass

    def run(self, results: Mapping[str, Any], log: bool = False) -> Dict[str, Any]:
        """Simply returns results and optionally logs them."""
        if log:
            for pod_name, response in results.items():
                for _, response_ in enumerate(response):
                    logger.info(f"{pod_name}: {response_['SUCCESS']}")

        return dict(results)


class _WorkerSide(BaseWorkerAlgorithm):
    """Worker side of the HuggingFaceTextLoraFineTuning algorithm."""

    def __init__(
        self,
        model_id: str,
        text_column_name: str,
        return_weights: bool,
        lora_r: int,
        lora_target_modules: Optional[List[str]],
        lora_alpha: int,
        lora_dropout: float,
        lora_bias: str,
        task_type: str,
        per_device_train_batch_size: int,
        gradient_accumulation_steps: int,
        warmup_steps: int,
        max_steps: int,
        learning_rate: float,
        logging_steps: float,
        optimizer: str,
        lr_scheduler_type: str,
        quantize: bool,
        fp16: bool,
        save_path: Union[str, os.PathLike] = BITFOUNT_OUTPUT_DIR,
        **kwargs: Any,
    ):
        super().__init__(**kwargs)
        self.model_id = model_id
        self.text_column_name = text_column_name
        self.return_weights = return_weights
        self.lora_r = lora_r
        self.lora_target_modules = lora_target_modules
        self.lora_alpha = lora_alpha
        self.lora_dropout = lora_dropout
        self.lora_bias = lora_bias
        self.task_type = task_type
        self.per_device_train_batch_size = per_device_train_batch_size
        self.gradient_accumulation_steps = gradient_accumulation_steps
        self.warmup_steps = warmup_steps
        self.max_steps = max_steps
        self.learning_rate = learning_rate
        self.logging_steps = logging_steps
        self.optimizer = optimizer
        self.lr_scheduler_type = lr_scheduler_type
        self.quantize = quantize
        self.fp16 = fp16
        self.save_path = Path(save_path)
        Path(self.save_path).mkdir(parents=True, exist_ok=True)

    def initialise(
        self,
        datasource: BaseSource,
        pod_dp: Optional[DPPodConfig] = None,
        pod_identifier: Optional[str] = None,
        **kwargs: Any,
    ) -> None:
        """Initialises the Lora Config for Fine-tuning.

        Creates tokenizer, tokenized datasource, base model,
        bits and bytes config, peft config.

        Args:
            datasource: The datasource to load as training dataset.
            pod_dp: The DP constrants to apply, not applicable for
                this algorithm. Defaults to None.
            pod_identifier: The identifier of the pod.
        """
        # TODO: [BIT-3097] Resolve initialise without DP
        if pod_dp:
            logger.warning("The use of DP is not supported, ignoring set `pod_dp`.")

        self.initialise_data(datasource=datasource)

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_id, trust_remote_code=True
        )
        self.tokenizer.pad_token = self.tokenizer.eos_token
        if self.fp16:
            self.tokenizer.padding_side = (
                "right"  # Fix weird overflow issue with fp16 training
            )

        # Convert pandas to hf dataset and tokenize.
        self.datasetdict = self._datasource_to_datasetdict(datasource=datasource).map(
            lambda samples: self.tokenizer(samples[self.text_column_name]), batched=True
        )

        # Quantization is currently supported on non-arm architectures.
        # Use BitsAndBytes Config only when quantization is enabled and
        # the architecture is non-arm.
        bnb_config = None
        if self.quantize:
            if platform.processor() in ("arm", "arm64"):
                logger.warning(
                    "Quantization is not supported on ARM architecture. "
                    + "Ignoring set `quantize`."
                )
                self.quantize = False
            else:
                bnb_config = BitsAndBytesConfig(
                    load_in_4bit=True,
                    bnb_4bit_use_double_quant=True,
                    bnb_4bit_quant_type="nf4",
                    bnb_4bit_compute_dtype=torch.bfloat16,
                )

        # Half-precision floating-point format is currently
        # supported on non-arm architectures.
        # Use it only when architecture is non-arm.
        if self.fp16:
            if platform.processor() in ("arm", "arm64"):
                logger.warning(
                    "Half-precision floating-point format is not supported "
                    + "on ARM architecture. Ignoring set `fp16`."
                )
                self.fp16 = False

        base_model = AutoModelForCausalLM.from_pretrained(
            self.model_id,
            quantization_config=bnb_config,
            trust_remote_code=True,
        )
        base_model.config.use_cache = False
        base_model.gradient_checkpointing_enable()
        base_model = prepare_model_for_kbit_training(base_model)

        peft_config = LoraConfig(
            r=self.lora_r,
            target_modules=self.lora_target_modules,
            lora_alpha=self.lora_alpha,
            lora_dropout=self.lora_dropout,
            bias=self.lora_bias,
            task_type=self.task_type,
        )
        self.peft_model = get_peft_model(base_model, peft_config)

    def _datasource_to_datasetdict(self, datasource: BaseSource) -> DatasetDict:
        """Convert a pandas dataframe to HuggingFace dataset.

        Necessary to allow training on HuggingFace models using
        `transformers.Trainer` `train_dataset`. Any data provided
        will be treatred as "training" set.

        Args:
            datasource: The datasource to load as training dataset.

        Returns:
            DatasetDict: The converted Datasource to DatasetDict.
        """
        ret = DatasetDict()
        ret["train"] = Dataset.from_pandas(datasource.get_data())
        return ret

    def run(self) -> Any:
        """Runs the pipeline to fine-tune a model."""

        training_args = TrainingArguments(
            per_device_train_batch_size=self.per_device_train_batch_size,
            gradient_accumulation_steps=self.gradient_accumulation_steps,
            warmup_steps=self.warmup_steps,
            max_steps=self.max_steps,
            learning_rate=self.learning_rate,
            logging_steps=self.logging_steps,
            optim=self.optimizer,
            lr_scheduler_type=self.lr_scheduler_type,
            fp16=self.fp16,
            output_dir=str(self.save_path),
            report_to="none",
        )

        trainer = Trainer(
            model=self.peft_model,
            train_dataset=self.datasetdict["train"],
            args=training_args,
            data_collator=DataCollatorForLanguageModeling(self.tokenizer, mlm=False),
        )

        trainer.train()

        if self.return_weights:  # TODO: [BIT-3286] Introduce protocol
            logger.warning(
                "Return of fine tuned model weights is not yet supported. "
                + "Fine tuned model will be saved locally instead."
            )
        trainer.model.save_pretrained(save_directory=str(self.save_path))
        message = "Model is saved locally"
        logger.info(f"SUCCESS, {message} at {str(self.save_path)}.")
        return trainer.state.log_history


class HuggingFaceTextLoraFineTuning(BaseAlgorithmFactory):
    """Hugging Face LoRA Fine Tuning Algorithm for Causal LMs.

    Args:
        model_id: The model id to use for transformer fine-tuning.
            The model id is of a pretrained model hosted inside a model
            repo on huggingface.co. Accepts models with a causal language
            modeling head.
        text_column_name: The signle column to train against. Should contain
            text for fine-tuning.
        lora_r: Lora attention dimension - the rank of the update matrices.
            Lower rank results in smaller update matrices with fewer
            trainable parameters.
        lora_target_modules: The names of the modules to apply Lora to.
        lora_alpha: Lora scaling factor.
        lora_dropout: The dropout probability for Lora layers.
        lora_bias: Specifies if the bias parameters should be trained
            Can be 'none', 'all' or 'lora_only'.
        task_type: The PEFT type of task to perform.
        per_device_train_batch_size: The batch size per GPU/TPU core/CPU for training.
        gradient_accumulation_steps: Number of updates steps to accumulate
            the gradients for, before performing a backward/update pass.
            When using gradient accumulation, one step is counted as one step with
            backward pass. Therefore, logging, evaluation, save will be conducted
            every `gradient_accumulation_steps * xxx_step` training examples.
        warmup_steps: Number of steps used for a linear warmup.
        max_steps: If set to a positive number, the total number of training steps
                to perform. Overrides `num_train_epochs`. In case of using
                a finite iterable dataset the training may stop before reaching
                the set number of steps when all data is exhausted.
        learning_rate: The initial learning rate for the optimizer.
        logging_steps: Number of update steps between two logs if
            `logging_strategy="steps"`. Should be an integer or a float
            in range `[0,1)`. If smaller than 1, will be interpreted as
            ratio of total training steps.
        optimizer: The optimizer to use.
        lr_scheduler_type: The scheduler type to use. See the documentation
            of [`SchedulerType`] for all possible values.
        quantize: Whether to use quantization config for loading the model (4-bit).
        fp16: Whether to use fp16 16-bit (mixed) precision training
            instead of 32-bit training.
        save_path: The output directory where the model predictions
            and checkpoints will be written.

    Attributes:
        model_id: The model id to use for transformer fine-tuning.
            The model id is of a pretrained model hosted inside a model
            repo on huggingface.co. Accepts models with a causal language
            modeling head.
        text_column_name: The signle column to train against. Should contain
            text for fine-tuning.
        lora_r: Lora attention dimension - the rank of the update matrices.
            Lower rank results in smaller update matrices with fewer
            trainable parameters.
        lora_target_modules: The names of the modules to apply Lora to.
        lora_alpha: Lora scaling factor.
        lora_dropout: The dropout probability for Lora layers.
        lora_bias: Specifies if the bias parameters should be trained
            Can be 'none', 'all' or 'lora_only'.
        task_type: The PEFT type of task to perform.
        per_device_train_batch_size: The batch size per GPU/TPU core/CPU for training.
        gradient_accumulation_steps: Number of updates steps to accumulate
            the gradients for, before performing a backward/update pass.
            When using gradient accumulation, one step is counted as one step with
            backward pass. Therefore, logging, evaluation, save will be conducted
            every `gradient_accumulation_steps * xxx_step` training examples.
        warmup_steps: Number of steps used for a linear warmup.
        max_steps: If set to a positive number, the total number of training steps
                to perform. Overrides `num_train_epochs`. In case of using
                a finite iterable dataset the training may stop before reaching
                the set number of steps when all data is exhausted.
        learning_rate: The initial learning rate for the optimizer.
        logging_steps: Number of update steps between two logs if
            `logging_strategy="steps"`. Should be an integer or a float
            in range `[0,1)`. If smaller than 1, will be interpreted as
            ratio of total training steps.
        optimizer: The optimizer to use.
        lr_scheduler_type: The scheduler type to use. See the documentation
            of [`SchedulerType`] for all possible values.
        quantize: Whether to use quantization config for loading the model (4-bit).
        fp16: Whether to use fp16 16-bit (mixed) precision training
            instead of 32-bit training.
        save_path: The output directory where the model predictions
            and checkpoints will be written.

    """

    fields_dict: ClassVar[T_FIELDS_DICT] = {
        "model_id": fields.Str(required=True),
        "text_column_name": fields.Str(required=True),
        "return_weights": fields.Boolean(
            required=False, missing=DEFAULT_RETURN_WEIGHTS
        ),
        "lora_r": fields.Int(required=False, missing=DEFAULT_LORA_R),
        "lora_target_modules": fields.List(fields.Str(), required=False, missing=None),
        "lora_alpha": fields.Int(required=False, missing=DEFAULT_LORA_ALPHA),
        "lora_dropout": fields.Float(required=False, missing=DEFAULT_LORA_DROPOUT),
        "lora_bias": fields.Str(required=False, missing=DEFAULT_LORA_BIAS),
        "task_type": fields.Str(required=False, missing=DEFAULT_TASK_TYPE),
        "per_device_train_batch_size": fields.Int(
            required=False, missing=DEFAULT_PER_DEVICE_TRAIN_BATCH_SIZE
        ),
        "gradient_accumulation_steps": fields.Int(
            required=False, missing=DEFAULT_GRADIENT_ACCUMULATION_STEPS
        ),
        "warmup_steps": fields.Int(required=False, missing=DEFAULT_WARMUP_STEPS),
        "max_steps": fields.Int(required=False, missing=DEFAULT_MAX_STEPS),
        "learning_rate": fields.Float(required=False, missing=DEFAULT_LEARNING_RATE),
        "logging_steps": fields.Float(required=False, missing=DEFAULT_LOGGING_STEPS),
        "optimizer": fields.Str(required=False, missing=DEFAULT_OPTIMIZER),
        "lr_scheduler_type": fields.Str(
            required=False, missing=DEFAULT_LR_SCHEDULER_TYPE
        ),
        "quantize": fields.Bool(require=False, missing=False),
        "fp16": fields.Bool(require=False, missing=False),
        "save_path": fields.Str(required=False, missing=BITFOUNT_OUTPUT_DIR),
    }

    def __init__(
        self,
        model_id: str,
        text_column_name: str,
        return_weights: bool = DEFAULT_RETURN_WEIGHTS,
        lora_r: int = DEFAULT_LORA_R,
        lora_target_modules: Optional[List[str]] = None,
        lora_alpha: int = DEFAULT_LORA_ALPHA,
        lora_dropout: float = DEFAULT_LORA_DROPOUT,
        lora_bias: str = DEFAULT_LORA_BIAS,
        task_type: str = DEFAULT_TASK_TYPE,
        per_device_train_batch_size: int = DEFAULT_PER_DEVICE_TRAIN_BATCH_SIZE,
        gradient_accumulation_steps: int = DEFAULT_GRADIENT_ACCUMULATION_STEPS,
        warmup_steps: int = DEFAULT_WARMUP_STEPS,
        max_steps: int = DEFAULT_MAX_STEPS,
        learning_rate: float = DEFAULT_LEARNING_RATE,
        logging_steps: float = DEFAULT_LOGGING_STEPS,
        optimizer: str = DEFAULT_OPTIMIZER,
        lr_scheduler_type: str = DEFAULT_LR_SCHEDULER_TYPE,
        quantize: bool = False,
        fp16: bool = False,
        save_path: Union[str, os.PathLike] = BITFOUNT_OUTPUT_DIR,
        **kwargs: Any,
    ):
        super().__init__(**kwargs)
        self.model_id = model_id
        self.text_column_name = text_column_name
        self.return_weights = return_weights
        self.lora_r = lora_r
        self.lora_target_modules = lora_target_modules
        self.lora_alpha = lora_alpha
        self.lora_dropout = lora_dropout
        self.lora_bias = lora_bias
        self.task_type = task_type
        self.per_device_train_batch_size = per_device_train_batch_size
        self.gradient_accumulation_steps = gradient_accumulation_steps
        self.warmup_steps = warmup_steps
        self.max_steps = max_steps
        self.learning_rate = learning_rate
        self.logging_steps = logging_steps
        self.optimizer = optimizer
        self.lr_scheduler_type = lr_scheduler_type
        self.quantize = quantize
        self.fp16 = fp16
        self.save_path = save_path

    def modeller(self, **kwargs: Any) -> _ModellerSide:
        """Returns the modeller side of the HuggingFaceTextLoraFineTuning algorithm."""
        return _ModellerSide(**kwargs)

    def worker(self, **kwargs: Any) -> _WorkerSide:
        """Returns the worker side of the HuggingFaceTextLoraFineTuning algorithm."""
        return _WorkerSide(
            model_id=self.model_id,
            text_column_name=self.text_column_name,
            return_weights=self.return_weights,
            lora_r=self.lora_r,
            lora_target_modules=self.lora_target_modules,
            lora_alpha=self.lora_alpha,
            lora_dropout=self.lora_dropout,
            lora_bias=self.lora_bias,
            task_type=self.task_type,
            per_device_train_batch_size=self.per_device_train_batch_size,
            gradient_accumulation_steps=self.gradient_accumulation_steps,
            warmup_steps=self.warmup_steps,
            max_steps=self.max_steps,
            learning_rate=self.learning_rate,
            logging_steps=self.logging_steps,
            optimizer=self.optimizer,
            lr_scheduler_type=self.lr_scheduler_type,
            quantize=self.quantize,
            fp16=self.fp16,
            save_path=self.save_path,
            **kwargs,
        )
