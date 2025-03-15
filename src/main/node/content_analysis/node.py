from typing import Dict, List, cast
import json
import re

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.runnables import RunnableConfig
from main.utils.chat_models import init_chat_model
from main.utils.constants import CONTENT_ANALYSIS_MODEL, CONTENT_ANALYSIS_TEMPERATURE

from .config import Configuration
from .state import ContentAnalysisState, ContentAnalysisOutput
from .prompt import SYSTEM_PROMPT
from main.utils.tools import SEARCH_TOOL
from langchain_core.messages import AIMessage


async def content_analysis(
    state: ContentAnalysisState, config: RunnableConfig
) -> Dict[str, List[AIMessage]]:
    """Analyze the content of an image.

    This function processes a base64 image, extracts text, identifies key content,
    and determines the language of the text in the image.

    Args:
        state (ContentAnalysisState): The current state of the conversation, containing the base64 image.
        config (RunnableConfig): Configuration for the model run.

    Returns:
        dict: A dictionary containing the model's response message with structured analysis.
    """
    configuration = Configuration.from_runnable_config(config)
    
    # Use model from configuration if specified, otherwise use the constant
    model_name = configuration.model if configuration.model else CONTENT_ANALYSIS_MODEL
    model = init_chat_model(model_name, temperature=CONTENT_ANALYSIS_TEMPERATURE)
    model_with_struct = model.with_structured_output(ContentAnalysisOutput)

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(
            content=[{"type": "image_url", "image_url": {"url": f"{state.image_url}"}}]
        ),
    ]

    if state.messages:
        messages.extend(state.messages)

    structured_output = await model_with_struct.ainvoke(messages, config)

    # Default should_evaluate to True if not specified
    should_evaluate = getattr(state, 'should_evaluate', True)
    export_folder = getattr(state, 'export_folder', '/export')
    
    return {
        "analysis_output": structured_output,
        "should_evaluate": should_evaluate,
        "export_folder": export_folder
    }
