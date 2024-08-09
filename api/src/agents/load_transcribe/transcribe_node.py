from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

from api.src.prompts.transcribe import transcribe_prompt
from api.src.agents.load_transcribe.state import State
from api.src.agents.load_transcribe.model import model


def transcribe_node(state: State):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", transcribe_prompt),
            HumanMessagePromptTemplate.from_template(
                template=[
                    {
                        "image_url": "{encoded_image_url}",
                    },
                ]
            ),
        ]
    )
    chain = prompt | model
    transcription = chain.invoke(
        input={
            "encoded_image_url": f"data:{state["mime_type"]};base64,{state["base_64_string"]}"
        }
    )
    return {"transcription": transcription.content, type: "basic"}
