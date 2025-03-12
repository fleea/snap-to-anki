from pydantic import BaseModel, Field
from typing import List, Optional, Literal

from main.state import InputState

CONTENT_TYPES = Literal["question_answer", "question_answer_multiple_choice", "vocabulary_table", "text", "image_caption", "decorative_image"]

class ContentSegment(BaseModel):
    type: CONTENT_TYPES
    transcription: str = Field(description="Content segment transcription")
    instructions: Optional[str] = Field(
        description="Optional instruction for flashcard creator node downstream"
    )
    is_decorative: bool = Field(
        description="Whether the content is decorative. If the segment seems not important, it will not be added on flashcard collection.")

class ContentAnalysisOutput(BaseModel):
    """
    Always use this tool to structure your response to the user.
    Structured output for content analysis of an image.
    """
    content: List[ContentSegment] = Field(
        description="Content types detected in the image"
    )
    language: str = Field(description="The language of the text in the image")


class ContentAnalysisState(InputState):
    """
    State for content analysis processing.
    """
