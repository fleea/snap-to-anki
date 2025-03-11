from typing import Dict, List
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from .state import FlashcardWriterState, Flashcard, FlashcardWriterOutput
from .prompt import SYSTEM_PROMPT
from .config import Configuration

from langchain.chat_models import init_chat_model
from typing import List


async def flashcard_writer(
    state: FlashcardWriterState, config: RunnableConfig
) -> Dict[str, List[AIMessage]]:
    """Convert analyzed content into Anki flashcards"""
    configuration = Configuration.from_runnable_config(config)

    model = init_chat_model(configuration.model, temperature=0.2)
    model_with_struct = model.with_structured_output(FlashcardWriterOutput)

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(
            content=[
                {
                    "type": "text",
                    "text": f"""
            Analysis Results:
            {state.analysis_output.model_dump_json(indent=2)}
            """,
                }
            ]
        ),
    ]

    output = await model_with_struct.ainvoke(messages, config)

    return {"flashcards": output.flashcards}
