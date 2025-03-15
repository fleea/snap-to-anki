from typing import List, Optional, Literal, Dict, Any
from pydantic import BaseModel, Field
from main.node.content_analysis.state import ContentAnalysisOutput
from main.state import InputState

class EvaluationResult(BaseModel):
    feedback: str = Field(description="Feedback on the flashcard content")
    next_step: Literal["exporter", "writer"] = Field(
        description="The suggested next step in the pipeline based on evaluation result"
    )

class FlashcardEvaluatorState(InputState):
    analysis_output: ContentAnalysisOutput = Field(description="Output from content analysis")
    csv: str = Field(description="CSV content containing the flashcards")
    evaluation_result: Optional[EvaluationResult] = None
