from typing import List, Optional, Literal
from pydantic import BaseModel, Field
from main.node.content_analysis.state import ContentAnalysisOutput
from main.state import State

class FlashcardWriterOutput(BaseModel):
    csv: str = Field(description="CSV content generated from the flashcard writer")

class FlashcardWriterState(FlashcardWriterOutput, State):
    analysis_output: ContentAnalysisOutput
    