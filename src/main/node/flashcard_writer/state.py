from typing import List, Optional, Literal
from pydantic import BaseModel, Field
from main.node.content_analysis.state import ContentAnalysisOutput

class FlashcardWriterOutput(BaseModel):
    csv: str = Field(description="CSV content generated from the flashcard writer")

class FlashcardWriterState(FlashcardWriterOutput):
    analysis_output: ContentAnalysisOutput
    