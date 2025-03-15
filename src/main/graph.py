"""
Define an agent that will accept base64 of an image and return Anki flashcard
"""

from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode
from main.utils.constants import EVALUATOR_MAX_RETRY

from main.config import Configuration
from main.state import InputState, State
from main.utils.tools import SEARCH_TOOL
from main.node.content_analysis.node import content_analysis
from main.edge.route import route_model_output
from main.node.flashcard_writer.node import flashcard_writer
from main.node.flashcard_evaluator.node import flashcard_evaluator
from main.node.flashcard_exporter.node import flashcard_exporter

builder = StateGraph(State, input=InputState, config_schema=Configuration)

builder.add_node("content_analysis", content_analysis)
builder.add_node("flashcard_writer", flashcard_writer)
builder.add_node("flashcard_evaluator", flashcard_evaluator)
builder.add_node("flashcard_exporter", flashcard_exporter)

def writer_router(state):
    # Get evaluation_retry_count if it exists, otherwise use default
    evaluation_retry_count = getattr(state, 'evaluation_retry_count', 0)
    
    # Default should_evaluate to True if not specified
    should_evaluate = getattr(state, 'should_evaluate', True)
    
    if should_evaluate and evaluation_retry_count <= EVALUATOR_MAX_RETRY:
        return "flashcard_evaluator"
    else:
        return "flashcard_exporter"

def evaluator_router(state):
    # Get evaluation state variables if they exist, otherwise use defaults
    passed_evaluation = getattr(state, 'passed_evaluation', False)
    evaluation_retry_count = getattr(state, 'evaluation_retry_count', 0)
    
    if passed_evaluation:
        return "flashcard_exporter"
    
    if evaluation_retry_count < EVALUATOR_MAX_RETRY:
        if hasattr(state, 'evaluation_result') and state.evaluation_result and \
           "content analysis" in state.evaluation_result.feedback.lower():
            return "content_analysis"
        else:
            return "flashcard_writer"
    else:
        return "flashcard_exporter"

builder.add_edge("__start__", "content_analysis")
builder.add_edge("content_analysis", "flashcard_writer")
builder.add_conditional_edges("flashcard_writer", writer_router, {
    "flashcard_evaluator": "flashcard_evaluator",
    "flashcard_exporter": "flashcard_exporter"
})
builder.add_conditional_edges("flashcard_evaluator", evaluator_router, {
    "flashcard_writer": "flashcard_writer",
    "content_analysis": "content_analysis",
    "flashcard_exporter": "flashcard_exporter"
})
builder.add_edge("flashcard_exporter", "__end__")

# Compile the builder into an executable graph
# You can customize this by adding interrupt points for state updates
graph = builder.compile(
    interrupt_before=[],
    interrupt_after=[],
)
graph.name = "Snapshot to Anki"
