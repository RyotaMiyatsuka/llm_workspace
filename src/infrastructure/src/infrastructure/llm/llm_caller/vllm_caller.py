from pydantic import BaseModel

from domain.domain_models.value_objects.prompt import Messages
from domain.interfaces.llm.llm_caller import ILlmCaller


class VLLMCaller(ILlmCaller):
    """vLLMを使ったLLM呼び出し."""

    def generate(
        self,
        messages: Messages,
        response_format: dict | BaseModel,
        response_choices: list,
    ) -> str:
        """LLM呼び出し."""
        # TODO
        return "ダミー回答 by vLLM"
