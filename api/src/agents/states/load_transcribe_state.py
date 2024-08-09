from typing import Annotated, Sequence, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class LoadTranscribeState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    mime_type: str
    base_64_string: str
    transcription: str
    csv: str
    type: str
