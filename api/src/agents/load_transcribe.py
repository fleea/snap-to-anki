from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END

from api.src.utils.image_file import get_mime_type, get_base64_string
from .flashcard import flashcard_node
from .state import LoadTranscribeState
from .transcribe import transcribe_node

memory = MemorySaver()


def load_and_transcribe(file_path: str):
    # Workflow
    # Prompt + Image
    # Get transcription
    # Transcription + image --> csv
    workflow = StateGraph(LoadTranscribeState)
    workflow.add_node("transcribe", transcribe_node)
    workflow.add_node("flashcard", flashcard_node)
    # TODO: CSV AGENT
    # TODO: Conditional edge to continue generating the transcription or csv
    workflow.add_edge(START, "transcribe")
    workflow.add_edge("transcribe", "flashcard")
    workflow.add_edge("flashcard", END)

    app = workflow.compile()

    config = {"recursion_limit": 50}

    image_base64 = get_base64_string(file_path)
    image_mimetype = get_mime_type(file_path)
    if image_base64 and image_mimetype:
        # based on LoadTranscribeState
        inputs = {"base_64_string": image_base64, "mime_type": image_mimetype}
        for event in app.stream(inputs, config=config):
            print(event)
        # transcribe_agent = ChatPromptTemplate.from_messages(
        #     [
        #         ("system", transcribe_prompt),
        #         HumanMessagePromptTemplate.from_template(
        #             template=[
        #                 {
        #                     "image_url": "{encoded_image_url}",
        #                 },
        #             ]
        #         )
        #     ]
        # )
        # chain = transcribe_agent | model_openai_4o
        # encoded = get_data_url_from_image(file_path)
        # response = chain.invoke(input={"encoded_image_url": encoded})
        # print(response)


if __name__ == '__main__':
    load_and_transcribe()
