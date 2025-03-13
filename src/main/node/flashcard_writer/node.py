from typing import Dict, List, Any
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from .state import FlashcardWriterState, FlashcardWriterOutput
from .prompt import SYSTEM_PROMPT
from .config import Configuration

from langchain.chat_models import init_chat_model
from typing import List


async def flashcard_writer(
    state: FlashcardWriterState, config: RunnableConfig
) -> Dict[str, Any]:
    """Convert analyzed content into Anki flashcards"""
    configuration = Configuration.from_runnable_config(config)

    model = init_chat_model(configuration.model, temperature=0.8).with_structured_output(FlashcardWriterOutput)

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

    output = await model.ainvoke(messages, config)
    
    return {"csv": output.csv, "analysis_output": state.analysis_output}
