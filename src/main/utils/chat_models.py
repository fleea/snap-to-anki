"""Chat model utilities for the Snap-to-Anki application."""

import os
import logging
import requests
from typing import Any, Dict, Optional

from langchain_core.language_models.chat_models import BaseChatModel
from langchain.chat_models import init_chat_model as langchain_init_chat_model
from main.utils.constants import OPENROUTER_BASE_URL
from main.utils.langchain_openrouter import init_langchain_openrouter

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Enable HTTP request debugging
http_logger = logging.getLogger('urllib3')
http_logger.setLevel(logging.DEBUG)
requests_log = logging.getLogger('requests.packages.urllib3')
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

def init_chat_model(model_name: str, **kwargs) -> BaseChatModel:
    """Initialize a chat model with the given configuration.
    
    This function is a wrapper around LangChain's init_chat_model that adds
    support for OpenRouter API integration.
    
    Args:
        model_name: The name of the model to use. Format: "provider:model_name"
        **kwargs: Additional arguments to pass to the model constructor.
        
    Returns:
        The initialized chat model.
    """
    try:
        parts = model_name.split(":", 1)
        provider = parts[0] if len(parts) > 1 else None
        model = parts[1] if len(parts) > 1 else model_name
        
        # Handle OpenRouter integration
        if provider == "openrouter":
            return init_langchain_openrouter(model, **kwargs)
        else:
            logger.info(f"Using standard LangChain model: {model_name}")
            # Add verbose flag for standard models too
            if "verbose" not in kwargs:
                kwargs["verbose"] = True
            return langchain_init_chat_model(model_name, **kwargs)
    except Exception as e:
        logger.error(f"Error initializing chat model: {str(e)}")
        raise
