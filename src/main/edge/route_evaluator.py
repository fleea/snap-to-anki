from typing import Literal

from main.node.flashcard_evaluator.state import FlashcardEvaluatorState
from main.utils.constants import (
    EVALUATOR_MAX_RETRY,
    CONTENT_ANALYSIS_NODE,
    FLASHCARD_WRITER_NODE,
    FLASHCARD_EXPORTER_NODE
)


def route_evaluator(state: FlashcardEvaluatorState) -> Literal[FLASHCARD_WRITER_NODE, CONTENT_ANALYSIS_NODE, FLASHCARD_EXPORTER_NODE]:
    """
    Determine where to route after evaluation.
    
    Routing logic:
    1. If retry count >= max_retry, go to exporter
    2. If transcription score < 7, go to content analysis
    3. If format correctness != 10 or content completeness < 7, go to writer
    4. Otherwise, go to exporter
    
    Args:
        state: The current state
        
    Returns:
        Literal[FLASHCARD_WRITER_NODE, CONTENT_ANALYSIS_NODE, FLASHCARD_EXPORTER_NODE]: The next node to route to
    """
    # Get evaluation retry count if it exists, otherwise use default
    evaluation_retry_count = getattr(state, 'evaluation_retry_count', 0)
    
    # If we've reached the maximum number of retries, go to exporter
    if evaluation_retry_count >= EVALUATOR_MAX_RETRY:
        return FLASHCARD_EXPORTER_NODE

    # Check if we have evaluation results
    if hasattr(state, 'evaluation_result') and state.evaluation_result:
        # If transcription score is less than 7, go back to content analysis
        if state.evaluation_result.transcription < 7:
            return CONTENT_ANALYSIS_NODE
        
        # If format correctness is not 10 or content completeness is less than 7, go back to writer
        if state.evaluation_result.formatCorrectness != 10 or state.evaluation_result.contentCompleteness < 7:
            return FLASHCARD_WRITER_NODE
        
        # If all scores are good, go to exporter
        return FLASHCARD_EXPORTER_NODE
    
    # Default: if no evaluation result exists, go to writer
    return FLASHCARD_EXPORTER_NODE
