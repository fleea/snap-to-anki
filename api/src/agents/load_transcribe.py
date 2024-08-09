
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END

from api.src.agents.nodes.flashcard import flashcard_node
from api.src.agents.nodes.transcribe import transcribe_node
from api.src.agents.states.load_transcribe_state import LoadTranscribeState
from api.src.utils.image_file import get_base64_string, get_mime_type

memory = MemorySaver()


def get_graph():
    workflow = StateGraph(LoadTranscribeState)
    workflow.add_node("transcribe", transcribe_node)
    workflow.add_node("flashcard", flashcard_node)
    workflow.add_edge(START, "transcribe")
    # Next step would be to check if transcription is complete and to rerun (continue) if not
    # Then the transcription could be
    workflow.add_edge("transcribe", "flashcard")
    workflow.add_edge("flashcard", END)
    return workflow.compile(checkpointer=memory)


def load_and_transcribe(file_path: str):
    graph = get_graph()
    image_base64 = get_base64_string(file_path)
    image_mimetype = get_mime_type(file_path)
    inputs = {"base_64_string": image_base64, "mime_type": image_mimetype}
    for event in graph.stream(inputs):
        print(event)


if __name__ == '__main__':
    get_graph()
