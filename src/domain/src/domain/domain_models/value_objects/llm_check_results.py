from pydantic import BaseModel

from domain.common.value_define.enums import LLMCheckType


class LLMCheckResult(BaseModel, frozen=True):
    """LLMの入出力結果."""

    success: bool
    check_type: LLMCheckType
