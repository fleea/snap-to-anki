"""Define the configurable parameters for the agent."""

from __future__ import annotations
import os
from dataclasses import dataclass, field, fields
from typing import Annotated, Optional

from langchain_core.runnables import RunnableConfig, ensure_config
from main.utils.constants import CONTENT_ANALYSIS_MODEL, CONTENT_ANALYSIS_TEMPERATURE

@dataclass(kw_only=True)
class Configuration:
    """The configuration for the analysis agent."""

    model: Annotated[str, {"__template_metadata__": {"kind": "llm"}}] = field(
        default=CONTENT_ANALYSIS_MODEL,
        metadata={
            "description": "The name of the language model to use for the agent's main interactions."
        }
    )
    
    temperature: Annotated[float, {"__template_metadata__": {"kind": "temperature"}}] = field(
        default=CONTENT_ANALYSIS_TEMPERATURE,
        metadata={
            "description": "The temperature to use for the language model."
        }
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
