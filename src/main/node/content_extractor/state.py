from pydantic import BaseModel, Field
from typing import List, Optional, Literal, Dict, Any

from main.state import State

CONTENT_TYPES = Literal["question_answer", "question_answer_multiple_choice", "vocabulary_table", "text", "image_caption", "decorative_image"]

class ContentSegment(BaseModel):
    type: CONTENT_TYPES
    transcription: str = Field(description="Content segment transcription")
    instructions: Optional[str] = Field(
        description="Optional instruction for flashcard creator node downstream"
    )
    is_decorative: bool = Field(
        description="Whether the content is decorative OR general instruction. If the segment seems not important, it will not be added on flashcard collection.")

class ContentAnalysisOutput(State):
    """
    Always use this tool to structure your response to the user.
    Structured output for content analysis of an image.
    """
    title: str = Field(description="Title of the image, separated with underscore")
    content: List[ContentSegment] = Field(
        description="Content types detected in the image"
    )
    language: str = Field(description="The language of the text in the image")


class ContentExtractorState(State):
    """
    State for content extraction processing.
    """
