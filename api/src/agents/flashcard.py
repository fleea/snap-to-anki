# from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
#
# from api.src.prompts.transcribe import transcribe_prompt
from .state import LoadTranscribeState


def flashcard_node(state: LoadTranscribeState):
    print("RUN FLASHCARD NODE")
    print(state["transcription"])
    print(state["mime_type"])
    # prompt = ChatPromptTemplate.from_messages(
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
    # chain = prompt | model
    # transcription = chain.invoke(
    #     input={"encoded_image_url": f"data:{state["mime_type"]};base64,{state["base_64_string"]}"})
    # return {"csv": transcription.content}
    return {}
