from pydantic import BaseModel, Field
from typing import List, Optional

from main.state import InputState


class ContentAnalysisOutput(BaseModel):
    """
    Always use this tool to structure your response to the user.
    Structured output for content analysis of an image.
    """

    extracted_text: str = Field(description="All text extracted from the image")
    key_content: str = Field(
        description="A summary of the key content or information in the image"
    )
    language: str = Field(description="The language of the text in the image")


class ContentAnalysisState(InputState):
    """
    State for content analysis processing.
    """
