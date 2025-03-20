"""
Define an agent that will accept base64 of an image and return Anki flashcard
"""

from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode
from main.utils.constants import (
    CONTENT_EXTRACTOR_NODE,
    CONTENT_ANALYSIS_NODE,
    FLASHCARD_WRITER_NODE,
    FLASHCARD_EVALUATOR_NODE,
    FLASHCARD_EXPORTER_NODE
)

from main.config import Configuration
from main.state import InputState, State
from main.node.content_extractor.node import content_extractor
from main.node.content_analysis.node import content_analysis
from main.node.flashcard_writer.node import flashcard_writer
from main.node.flashcard_evaluator.node import flashcard_evaluator
from main.node.flashcard_exporter.node import flashcard_exporter
from main.edge.route_writer import route_writer
from main.edge.route_evaluator import route_evaluator

builder = StateGraph(State, input=InputState, config_schema=Configuration)

builder.add_node(CONTENT_EXTRACTOR_NODE, content_extractor)
builder.add_node(CONTENT_ANALYSIS_NODE, content_analysis)
builder.add_node(FLASHCARD_WRITER_NODE, flashcard_writer)
builder.add_node(FLASHCARD_EVALUATOR_NODE, flashcard_evaluator)
builder.add_node(FLASHCARD_EXPORTER_NODE, flashcard_exporter)

builder.add_edge("__start__", CONTENT_EXTRACTOR_NODE)
builder.add_edge(CONTENT_EXTRACTOR_NODE, CONTENT_ANALYSIS_NODE)
builder.add_edge(CONTENT_ANALYSIS_NODE, FLASHCARD_WRITER_NODE)
builder.add_conditional_edges(FLASHCARD_WRITER_NODE, route_writer, {
    FLASHCARD_EVALUATOR_NODE: FLASHCARD_EVALUATOR_NODE,
    FLASHCARD_EXPORTER_NODE: FLASHCARD_EXPORTER_NODE
})
builder.add_conditional_edges(FLASHCARD_EVALUATOR_NODE, route_evaluator, {
    FLASHCARD_WRITER_NODE: FLASHCARD_WRITER_NODE,
    CONTENT_ANALYSIS_NODE: CONTENT_ANALYSIS_NODE,
    FLASHCARD_EXPORTER_NODE: FLASHCARD_EXPORTER_NODE
})
builder.add_edge(FLASHCARD_EXPORTER_NODE, "__end__")

# Compile the builder into an executable graph
# You can customize this by adding interrupt points for state updates
graph = builder.compile(
    interrupt_before=[],
    interrupt_after=[],
)
graph.name = "Snapshot to Anki"
