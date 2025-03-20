from __future__ import annotations
from pydantic import Field
from typing import List, Dict, Any, Sequence, Optional
from dataclasses import dataclass, field

from langchain_core.messages import AnyMessage
from langgraph.graph import add_messages
from typing_extensions import Annotated


@dataclass
class ConfigState:
    """Defines the configuration state that will be shared across all nodes.
    
    This class contains configuration options that should be accessible to all nodes.
    """
    pass


@dataclass
class InputState(ConfigState):
    """Defines the input state for the agent, representing a narrower interface to the outside world.

    This class is used to define the initial state and structure of incoming data.
    Only includes fields that should be directly provided by the user.
    """
    url: str
    should_evaluate: bool = True
    export_folder: str = "/export"

    messages: Annotated[Sequence[AnyMessage], add_messages] = field(
        default_factory=list
    )
    """
    Messages tracking the primary execution state of the agent.

    Typically accumulates a pattern of:
    1. HumanMessage - user input
    2. AIMessage with .tool_calls - agent picking tool(s) to use to collect information
    3. ToolMessage(s) - the responses (or errors) from the executed tools
    4. AIMessage without .tool_calls - agent responding in unstructured format to the user
    5. HumanMessage - user responds with the next conversational turn

    Steps 2-5 may repeat as needed.

    The `add_messages` annotation ensures that new messages are merged with existing ones,
    updating by ID to maintain an "append-only" state unless a message with the same ID is provided.
    """


@dataclass
class State(InputState):
    """Represents the complete state of the agent, extending InputState with additional attributes.

    This class can be used to store any information needed throughout the agent's lifecycle.
    Includes fields that are generated during processing and not directly provided by the user.
    """
    # Fields for passing data between nodes
    analysis_output: Optional[dict] = None
    csv: Optional[str] = None
    evaluation_result: Optional[dict] = None
    
    # State tracking fields
    evaluation_retry_count: int = 0
    ocr_data: Dict[str, Any] = Field(description="List of Raw OCR data from Mistral AI or fallback LLM")
