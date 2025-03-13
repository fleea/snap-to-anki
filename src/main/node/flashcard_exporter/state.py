from typing import List, Optional, Literal
from pydantic import BaseModel, Field
from main.node.content_analysis.state import ContentAnalysisOutput

class FlashcardExporterState(BaseModel):
    analysis_output: ContentAnalysisOutput
    csv: str = Field(description="CSV content containing the flashcards")