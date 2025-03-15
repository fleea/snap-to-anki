from typing import List, Optional, Literal
from pydantic import BaseModel, Field
from main.node.content_analysis.state import ContentAnalysisOutput
from main.state import InputState

class FlashcardWriterOutput(BaseModel):
    csv: str = Field(description="CSV content generated from the flashcard writer")

class FlashcardWriterState(FlashcardWriterOutput, InputState):
    analysis_output: ContentAnalysisOutput
    