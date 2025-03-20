from typing import Dict, List, cast
import json
import re
import aiohttp

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.runnables import RunnableConfig
from main.utils.chat_models import init_chat_model
from main.utils.constants import CONTENT_EXTRACTOR_MODEL, CONTENT_EXTRACTOR_TEMPERATURE

from .config import Configuration
from .prompt import SYSTEM_PROMPT
from .state import ContentExtractorState
from main.tool import pdf_ocr, image_ocr
from main.tool.pdf_ocr import OCRResponse
from main.utils.logger import logger


async def content_extractor(
    state: ContentExtractorState, config: RunnableConfig
) -> Dict[str, List[AIMessage]]:
    configuration = Configuration.from_runnable_config(config)
    
    model_name = configuration.model if configuration.model else CONTENT_EXTRACTOR_MODEL
    model = init_chat_model(model_name, temperature=CONTENT_EXTRACTOR_TEMPERATURE)

    url = state.url
    async with aiohttp.ClientSession() as session:
        async with session.head(url) as response:
            content_type = response.headers.get('Content-Type', '')

    if 'application/pdf' in content_type:
        ocr_response = pdf_ocr(url)
    elif 'image/' in content_type:
        logger.info(f"Using image_ocr for URL: {url}")
        ocr_response = image_ocr(url)
    else:
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(
                content=[{"type": "image_url", "image_url": {"url": f"{url}"}}]
            ),
        ]
        if state.messages:
            messages.extend(state.messages)

        ocr_response = cast(
            AIMessage,
            await model.ainvoke(messages, config),
        )

    return {"ocr_data": [ocr_response]}
