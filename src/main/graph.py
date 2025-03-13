"""
Define an agent that will accept base64 of an image and return Anki flashcard
"""

from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode

from main.config import Configuration
from main.state import InputState, State
from main.utils.tools import SEARCH_TOOL
from main.node.content_analysis.node import content_analysis
from main.edge.route import route_model_output
from main.node.flashcard_writer.node import flashcard_writer
from main.node.flashcard_exporter.node import flashcard_exporter

builder = StateGraph(State, input=InputState, config_schema=Configuration)

builder.add_node("content_analysis", content_analysis)
builder.add_node("flashcard_writer", flashcard_writer)
builder.add_node("flashcard_exporter", flashcard_exporter)

builder.add_edge("__start__", "content_analysis")
builder.add_edge("content_analysis", "flashcard_writer")
builder.add_edge("flashcard_writer", "flashcard_exporter")
builder.add_edge("flashcard_exporter", "__end__")

# Compile the builder into an executable graph
# You can customize this by adding interrupt points for state updates
graph = builder.compile(
    interrupt_before=[],
    interrupt_after=[],
)
graph.name = "Snapshot to Anki"
