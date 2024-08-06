from typing import Annotated, Sequence, TypedDict

from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI
from langgraph.graph.message import add_messages

from api.src.utils.constants import openai_key


class LoadTranscribeState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]
    mime_type: str
    base_64_string: str
    transcription: str


# USED IN MANY AGENT
model = ChatOpenAI(model="gpt-4o", temperature=0, api_key=openai_key)
