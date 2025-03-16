from typing import Literal

from main.node.flashcard_evaluator.state import FlashcardEvaluatorState
from main.utils.constants import EVALUATOR_MAX_RETRY, FLASHCARD_WRITER_NODE, FLASHCARD_EVALUATOR_NODE, FLASHCARD_EXPORTER_NODE


def route_writer(state: FlashcardEvaluatorState) -> Literal[FLASHCARD_EVALUATOR_NODE, FLASHCARD_EXPORTER_NODE]:
    """
    Determine whether to route from writer to evaluator or exporter.
    
    Routing logic:
    1. If should_evaluate is True and evaluation_retry_count <= EVALUATOR_MAX_RETRY, go to evaluator
    2. Otherwise, go to exporter
    
    Args:
        state: The current state
        
    Returns:
        Literal[FLASHCARD_EVALUATOR_NODE, FLASHCARD_EXPORTER_NODE]: The next node to route to
    """
    # Get evaluation_retry_count if it exists, otherwise use default
    evaluation_retry_count = getattr(state, 'evaluation_retry_count', 0)
    
    # Default should_evaluate to True if not specified
    should_evaluate = getattr(state, 'should_evaluate', True)
    
    if should_evaluate and evaluation_retry_count <= EVALUATOR_MAX_RETRY:
        return FLASHCARD_EVALUATOR_NODE
    else:
        return FLASHCARD_EXPORTER_NODE
