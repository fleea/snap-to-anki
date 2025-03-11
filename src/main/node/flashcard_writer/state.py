from typing import List, Optional, Literal
from pydantic import BaseModel, Field
from main.node.content_analysis.state import ContentAnalysisOutput


class Flashcard(BaseModel):
    front: str = Field(description="Question of the card")
    back: str = Field(description="Answer of the card")
    card_type: Literal["basic", "cloze"] = Field(
        description="Type of card", default="basic"
    )


class FlashcardWriterState(BaseModel):
    analysis_output: ContentAnalysisOutput
    flashcards: List[Flashcard] = []


class FlashcardWriterOutput(BaseModel):
    flashcards: List[Flashcard] = Field(
        description="List of flashcards generated from the content analysis"
    )
