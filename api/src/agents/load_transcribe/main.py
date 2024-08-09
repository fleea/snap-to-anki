from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END

from api.src.agents.load_transcribe.flashcard_node import flashcard_node
from api.src.agents.load_transcribe.transcribe_node import transcribe_node
from api.src.agents.load_transcribe.state import State
from api.src.utils.image_file import get_base64_string, get_mime_type

memory = MemorySaver()


# Idea for next step:
# - Transcribe node : check if transcription is complete and to continue if not
# - Flashcard node : check if all content has been covered, continue if not
# - Prioritize the content
# - RAG style (get previous/next/related pages) for extra context so it won't be cut off
# - Cut/cover image for image based flashcard

def get_graph():
    workflow = StateGraph(State)
    workflow.add_node("transcribe", transcribe_node)
    workflow.add_node("flashcard", flashcard_node)
    workflow.add_edge(START, "transcribe")
    workflow.add_edge("transcribe", "flashcard")
    workflow.add_edge("flashcard", END)
    return workflow.compile(checkpointer=memory)


def load_and_transcribe(file_path: str):
    graph = get_graph()
    config = {"configurable": {"thread_id": file_path}}
    image_base64 = get_base64_string(file_path)
    image_mimetype = get_mime_type(file_path)
    inputs = {"base_64_string": image_base64, "mime_type": image_mimetype}
    state: State = graph.invoke(inputs, config=config)
    return state


if __name__ == "__main__":
    get_graph()
