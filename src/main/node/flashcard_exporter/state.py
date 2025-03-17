from typing import List, Optional, Literal
from pydantic import BaseModel, Field
from main.node.content_analysis.state import ContentAnalysisOutput
from main.state import State

class FlashcardExporterState(BaseModel, State):
    analysis_output: ContentAnalysisOutput
    csv: str = Field(description="CSV content containing the flashcards")