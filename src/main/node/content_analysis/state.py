from pydantic import BaseModel, Field
from typing import List, Optional, Literal

from main.state import InputState


class ContentAnalysisOutput(BaseModel):
    """
    Always use this tool to structure your response to the user.
    Structured output for content analysis of an image.
    """

    extracted_text: str = Field(description="All text extracted from the image")
    content_types: List[Literal["questions", "vocabulary_table", "formulas"]] = Field(
        description="Content types detected in the image"
    )
    language: str = Field(description="The language of the text in the image")
    formatting_requirements: List[str] = Field(
        description="Requirements for formatting the content [use_latex, preserve_numbering, ...]"
    )
    processing_instructions: str = Field(
        description="Directions for the flashcard creator node downstream"
    )


class ContentAnalysisState(InputState):
    """
    State for content analysis processing.
    """
