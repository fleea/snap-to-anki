from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from api.src.agents.states.load_transcribe_state import LoadTranscribeState
from api.src.prompts.basic import generate_basic_prompt_text
from api.src.prompts.system import base_system_template
from api.src.agents.models.main import model


def flashcard_node(state: LoadTranscribeState):
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", base_system_template),
            HumanMessagePromptTemplate.from_template("{txt}")
        ]
    )
    chain = prompt | model
    csv_request = chain.invoke(
        input={"txt": generate_basic_prompt_text(state["transcription"])})
    return {"csv": csv_request.content}
