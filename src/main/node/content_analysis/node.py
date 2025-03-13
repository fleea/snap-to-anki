from typing import Dict, List, cast
import json
import re

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.runnables import RunnableConfig
from main.utils.chat_models import init_chat_model

from .config import Configuration
from .state import ContentAnalysisState, ContentAnalysisOutput
from .prompt import SYSTEM_PROMPT
from main.utils.tools import SEARCH_TOOL
from langchain_core.messages import AIMessage
from typing import List


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
    model = init_chat_model(configuration.model, temperature=1)
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

    # Return the model's response as a list to be added to existing messages
    return {"analysis_output": structured_output}
