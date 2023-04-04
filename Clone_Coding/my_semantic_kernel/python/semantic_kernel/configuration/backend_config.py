from typing import Optional

from semantic_kernel.ai.open_ai.services.open_ai_config import OpenAIConifg
from semantic_kernel.configuration.backend_type import BackendType


class BackendConfig:
    backend_type: BackendType = BackendType.Unknown
    open_ai: Optional[OpenAIConifg] = None

    def __init__(
            self,
            backend_type: BackendType,
            open_ai: Optional[OpenAIConifg] = None
    ) -> None:
        self.backend_type = backend_type
        self.open_ai = open_ai