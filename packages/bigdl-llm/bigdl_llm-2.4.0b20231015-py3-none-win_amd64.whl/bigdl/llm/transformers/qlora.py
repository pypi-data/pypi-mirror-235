#
# Copyright 2016 The BigDL Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Some parts of this file is adapted from
# https://github.com/huggingface/peft/blob/v0.5.0/src/peft/tuners/lora.py
#
# coding=utf-8
# Copyright 2023-present the HuggingFace Inc. team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import torch
from bigdl.llm.transformers.low_bit_linear import LowBitLinear
from peft.tuners.lora import LoraLayer
from bigdl.llm.utils.common import invalidInputError
import functools


class LoraLowBitLinear(LowBitLinear, LoraLayer):
    # Lora implemented in a dense layer
    def __init__(
        self,
        adapter_name,
        in_features,
        out_features,
        r: int = 0,
        lora_alpha: int = 1,
        lora_dropout: float = 0.0,
        **kwargs,
    ):
        LowBitLinear.__init__(
            self,
            in_features,
            out_features,
            qtype=kwargs.get("qtype"),
            bias=kwargs.get("bias", True),
            conver_to_half=False,
        )
        LoraLayer.__init__(self, in_features=in_features, out_features=out_features)

        # Freezing the pre-trained weight matrix
        self.weight.requires_grad = False

        init_lora_weights = kwargs.pop("init_lora_weights", True)
        self.update_layer(adapter_name, r, lora_alpha, lora_dropout, init_lora_weights)
        self.active_adapter = adapter_name

    def forward(self, x: torch.Tensor):
        result = super().forward(x)

        if self.disable_adapters or self.active_adapter not in self.lora_A.keys():
            return result
        elif self.r[self.active_adapter] > 0:
            result = result.clone()
            if not torch.is_autocast_enabled():
                expected_dtype = result.dtype
                x = x.to(self.lora_A[self.active_adapter].weight.dtype)
                output = (
                    self.lora_B[self.active_adapter](
                        self.lora_A[self.active_adapter](self.lora_dropout[self.active_adapter](x))
                    ).to(expected_dtype)
                    * self.scaling[self.active_adapter]
                )
            else:
                output = (
                    self.lora_B[self.active_adapter](
                        self.lora_A[self.active_adapter](self.lora_dropout[self.active_adapter](x))
                    )
                    * self.scaling[self.active_adapter]
                )
            result += output
        return result


def _create_new_module(create_new_module_func, lora_config, adapter_name, target, **kwargs):

    if isinstance(target, LowBitLinear):
        low_bit_kwargs = kwargs.copy()
        bias = low_bit_kwargs.pop("bias", False)
        low_bit_kwargs.update(
            {
                "qtype": target.qtype,
            }
        )
        new_module = LoraLowBitLinear(adapter_name,
                                      target.in_features,
                                      target.out_features,
                                      bias=bias,
                                      **low_bit_kwargs)
    else:
        new_module = create_new_module_func(lora_config, adapter_name, target, **kwargs)

    return new_module


from peft.tuners.lora import LoraModel


def get_peft_model(*args, **kwargs):
    old_create_new_module = LoraModel._create_new_module
    LoraModel._create_new_module = staticmethod(functools.partial(_create_new_module,
                                                                  old_create_new_module))
    try:
        from peft import get_peft_model as get_peft_model_original
        model = get_peft_model_original(*args, **kwargs)
    finally:
        LoraModel._create_new_module = old_create_new_module

    return model


def prepare_model_for_kbit_training(model, use_gradient_checkpointing=True):
    r"""
    This method wraps the entire protocol for preparing a model before running a training.
    This includes:
        1- Cast the layernorm in fp32
        2- making output embedding layer require grads
        3- Add the upcasting of the lm head to fp32

    Args:
        model, (`transformers.PreTrainedModel`):
            The loaded model from `transformers`
    """

    is_gptq_quantized = getattr(model, "quantization_method", None) == "gptq"
    for name, param in model.named_parameters():
        # freeze base model's layers
        param.requires_grad = False

    if not is_gptq_quantized:
        # cast all non INT8 parameters to fp32
        for param in model.parameters():
            if (param.dtype == torch.float16) or (param.dtype == torch.bfloat16):
                param.data = param.data.to(torch.float32)

    if use_gradient_checkpointing:
        # For backward compatibility
        if hasattr(model, "enable_input_require_grads"):
            model.enable_input_require_grads()
        else:

            def make_inputs_require_grad(module, input, output):
                output.requires_grad_(True)

            model.get_input_embeddings().register_forward_hook(make_inputs_require_grad)

        # enable gradient checkpointing for memory efficiency
        model.gradient_checkpointing_enable()

    return model


class PeftModel:

    @staticmethod
    def from_pretrained(*args,
                        **kwargs):
        old_create_new_module = LoraModel._create_new_module
        LoraModel._create_new_module = staticmethod(functools.partial(_create_new_module,
                                                                      old_create_new_module))
        from peft import PeftModel
        try:
            model = PeftModel.from_pretrained(*args, **kwargs)
        finally:
            LoraModel._create_new_module = old_create_new_module

        return model


def patch_prepare_ipex(self, *args):
    return tuple(args)

# workaround a IPEX bug that prevents resume training in bf16
from accelerate import Accelerator
Accelerator._prepare_ipex = patch_prepare_ipex
