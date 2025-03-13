"""Define the configurable parameters for the agent."""

from __future__ import annotations

from dataclasses import dataclass, field, fields
from typing import Annotated, Optional
import os
from langchain_core.runnables import RunnableConfig, ensure_config

from dotenv import load_dotenv

load_dotenv()

@dataclass(kw_only=True)
class Configuration:
    """The configuration for the agent."""

    flashcard_writer_model: str = os.getenv("FLASHCARD_WRITER_MODEL", "openai:gpt-4o")
    model: Annotated[str, {"__template_metadata__": {"kind": "llm"}}] = field(
        default=flashcard_writer_model,
        metadata={
            "description": "The name of the language model to use for the agent's main interactions. "
            "Should be in the form: provider/model-name."
        },
    )
    flashcard_writer_temperature: float = float(os.getenv("FLASHCARD_WRITER_TEMPERATURE", "0.8"))
    temperature: Annotated[float, {"__template_metadata__": {"kind": "temperature"}}] = field(
        default=flashcard_writer_temperature,
        metadata={
            "description": "The temperature to use for the language model. "
            "Higher values make the output more random, lower values make it more focused."
        },
    )

    @classmethod
    def from_runnable_config(
        cls, config: Optional[RunnableConfig] = None
    ) -> Configuration:
        """Create a Configuration instance from a RunnableConfig object."""
        config = ensure_config(config)
        configurable = config.get("configurable") or {}
        _fields = {f.name for f in fields(cls) if f.init}
        return cls(**{k: v for k, v in configurable.items() if k in _fields})
