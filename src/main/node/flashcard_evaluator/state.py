from typing import List, Optional, Literal, Dict, Any
from pydantic import BaseModel, Field
from main.node.content_analysis.state import ContentAnalysisOutput
from main.state import State

class EvaluationScores(BaseModel):
    transcription: int = Field(description="Score for transcription accuracy (0-10)")
    formatCorrectness: int = Field(description="Score for format correctness (0-10)")
    contentCompleteness: int = Field(description="Score for content completeness (0-10)")

class EvaluationResult(BaseModel):
    transcription: int = Field(description="Score for transcription accuracy (0-10)")
    formatCorrectness: int = Field(description="Score for format correctness (0-10)")
    contentCompleteness: int = Field(description="Score for content completeness (0-10)")
    feedback: str = Field(description="Explanation of the evaluation")

class FlashcardEvaluatorState(State):
    analysis_output: ContentAnalysisOutput = Field(description="Output from content analysis")
    csv: str = Field(description="CSV content containing the flashcards")
    evaluation_result: Optional[EvaluationResult] = None
    evaluation_retry_count: int = Field(default=0, description="Number of times evaluation has been retried")
