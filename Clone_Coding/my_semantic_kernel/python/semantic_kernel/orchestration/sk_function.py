import asyncio
import threading
from enum import Enum
from logging import Logger
from typing import Any, Callable, List, Optional, cast

from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase
from semantic_kernel.connectors.ai.chat_request_settings import ChatRequestSettings
from semantic_kernel.connectors.ai.complete_request_settings import CompleteRequestSettings
from semantic_kernel.connectors.ai.text_completion_client_base import TextCompletionClientBase
from semantic_kernel.kernel_exception import KernelException
from semantic_kernel.memory.null_memory import NullMemory
from semantic_kernel.memory.semantic_text_memory_base import SemanticTextMemoryBase
from semantic_kernel.orchestration.context_variables import ContextVariables
from semantic_kernel.orchestration.delegate_handlers import DelegateHandlers
from semantic_kernel.orchestration.delegate_inference import DelegateInference
from semantic_kernel.orchestration.delegate_types import DelegateTypes
from semantic_kernel.orchestration.sk_context import SKContext
from semantic_kernel.orchestration.sk_function_base import SKFunctionBase
from semantic_kernel.semantic_functions.chat_prompt_template import ChatPromptTemplate
from semantic_kernel.semantic_functions.semantic_function_config import (
    SemanticFunctionConfig,
)
from semantic_kernel.skill_definition.function_view import FunctionView
from semantic_kernel.skill_definition.parameter_view import ParameterView
from semantic_kernel.skill_definition.read_only_skill_collection_base import (
    ReadOnlySkillCollectionBase,
)
from semantic_kernel.utils.null_logger import NullLogger


class SKFunction(SKFunctionBase):
    """
    Semantic Kernel function.
    """

    _parameters: List[ParameterView]
    _delegate_type: DelegateTypes
    _function: Callable[..., Any]
    _skill_collection: Optional[ReadOnlySkillCollectionBase]
    _log: Logger
    _ai_service: Optional[TextCompletionClientBase]
    _ai_request_settings: CompleteRequestSettings
    _chat_service: Optional[ChatCompletionClientBase]
    _chat_request_settings: ChatRequestSettings

    @staticmethod
    def from_native_method(method, skill_name="", log=None) -> "SKFunction":
        if method is None:
            raise ValueError("Method cannot be `None`")
        
        assert method.__sk_function__ is not None, "Method is not a SK function"
        assert method.__sk_function_name__ is not None, "Method name is empty"

        parameters = []
        # sk_function_context_parameters are optionals
        if hasattr(method, "__sk_function_context_parameters__"):
            for param in method.__sk_function_context_parameters__:
                assert "name" in param, "Parameter name is empty"
                assert "description" in param, "Parameter description is empty"
                assert "default_value" in param, "Parameter default value is empty"

                parameters.append(
                    ParameterView(
                        param["name"], param["description"], param["default_value"]
                    )
                )

        if hasattr(method, "__sk_function_input_description__"):
            input_param = ParameterView(
                "input",
                method.__sk_function_input_description__,
                method.__sk_function_input_default_value__,
            )
            parameters = [input_param] + parameters

        return SKFunction(
            delegate_type=DelegateInference.infer_delegate_type(method),
            delegate_function=method,
            parameters=parameters,
            description=method.__sk_function_description__,
            skill_name=skill_name,
            function_name=method.__sk_function_name__,
            is_semantic=False,
            log=log,
        )
    
    @staticmethod
    def from_semantic_config(
        skill_name: str,
        function_name: str,
        function_config: SemanticFunctionConfig,
        log: Optional[Logger] = None,
    ) -> "SKFunction":
        if function_config is None:
            raise ValueError("Function configuration cannot be `None`")
        
        async def _local_func(client, request_settings, context):
            if client is None:
                raise ValueError("AI LLM service cannot be `None`")
            
            try:
                if function_config.has_chat_prompt:
                    as_chat_prompt = cast(
                        ChatPromptTemplate, function_config.prompt_template
                    )

                    messages = await as_chat_prompt.render_messages_async(context)
                    completion = await client.complete_chat_async(
                        messages, request_settings
                    )

                    _, content = messages[-1]
                    as_chat_prompt.add_user_message(content)
                    as_chat_prompt.add_assistant_message(completion)

                    context.variables.update(completion)
                else:
                    prompt = await function_config.prompt_template.render_async(context)
                    completion = await client.complete_async(prompt, request_settings)
                    context.variables.update(completion)
            except Exception as e:
                context.fail(str(e), e)
            
            return context

        return SKFunction(
            delegate_type=DelegateTypes.ContextSwitchInSKContextOutTaskSKContext,
            delegate_function=_local_func,
            parameters=function_config.prompt_template.get_parameters(),
            description=function_config.prompt_template_config.description,
            skill_name=skill_name,
            function_name=skill_name,
            function_name=function_name,
            is_semantic=True,
            log=log,
        )
    
    