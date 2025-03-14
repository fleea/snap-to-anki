from typing import Literal

from langchain_core.messages import AIMessage

from main.state import InputState, State


def route_model_output(state: State) -> Literal["__end__", "tools"]:
    """Determine next step based on model output."""
    if not state.messages:
        raise ValueError("No messages in state")
    last_message = state.messages[-1]
    if not isinstance(last_message, AIMessage):
        raise ValueError(f"Expected AIMessage, got {type(last_message).__name__}")

    # Route tool calls to search
    if last_message.tool_calls:
        return "tools"

    # Otherwise wait for user input
    return "__end__"
