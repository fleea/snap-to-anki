from typing import Dict, List, Any
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from .state import FlashcardWriterState, FlashcardWriterOutput
from .config import Configuration
from main.utils.chat_models import init_chat_model
from main.utils.constants import FLASHCARD_WRITER_MODEL, FLASHCARD_WRITER_TEMPERATURE

from main.node.flashcard_writer.prompt import get_prompt_by_segment_type

# DOES NOT NEED STRUCTURED OUTPUT
async def flashcard_writer(
    state: FlashcardWriterState, config: RunnableConfig
) -> Dict[str, Any]:
    """Convert analyzed content into Anki flashcards"""
    configuration = Configuration.from_runnable_config(config)
    
    # Use model from configuration if specified, otherwise use the constant
    model_name = configuration.model if configuration.model else FLASHCARD_WRITER_MODEL
    model = init_chat_model(model_name, temperature=FLASHCARD_WRITER_TEMPERATURE)
    
    # Extract segment types from the analysis output
    segment_types = [segment.type for segment in state.analysis_output.content]
    
    # Get the specialized prompt based on segment types
    specialized_prompt = get_prompt_by_segment_type(segment_types)

    messages = [
        SystemMessage(content=specialized_prompt),
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
    
    # Get evaluation state variables if they exist, otherwise use defaults
    evaluation_retry_count = getattr(state, 'evaluation_retry_count', 0)
    passed_evaluation = getattr(state, 'passed_evaluation', False)
    
    return {
        "csv": output, 
        "analysis_output": state.analysis_output,
        "evaluation_retry_count": evaluation_retry_count,
        "passed_evaluation": passed_evaluation
    }
