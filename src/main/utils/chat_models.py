"""Chat model utilities for the Snap-to-Anki application."""

import os
import logging
import requests
from typing import Any, Dict, Optional

from langchain_openai import ChatOpenAI
from langchain_core.language_models.chat_models import BaseChatModel
from langchain.chat_models import init_chat_model as langchain_init_chat_model
from main.utils.constants import OPENROUTER_BASE_URL

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
            # Get OpenRouter API key from environment variables
            openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
            
            if not openrouter_api_key:
                logger.error("OPENROUTER_API_KEY environment variable is missing")
                raise ValueError(
                    "OPENROUTER_API_KEY environment variable is required for OpenRouter integration."
                )
            
            logger.info(f"Using OpenRouter with model: {model}")
            
            # Use the base URL from constants
            logger.info(f"OpenRouter base URL: {OPENROUTER_BASE_URL}")
            
            model_kwargs = {
                "model": model,
                "temperature": kwargs.get("temperature", 0.7),
                "openai_api_key": openrouter_api_key,
                "base_url": OPENROUTER_BASE_URL,
                "default_headers": {
                    "HTTP-Referer": "https://snap-to-anki.local",
                    "X-Title": "Snap-to-Anki"
                },
                "max_retries": 3,
                "request_timeout": 120,
                "verbose": True,  # Enable verbose mode to see more details
            }

            # Create a debug wrapper function to intercept and log requests
            def _log_request_info(request, *args, **kwargs):
                logger.debug(f"Making request to: {request.url}")
                logger.debug(f"Request method: {request.method}")
                logger.debug(f"Request headers: {request.headers}")
                return request
            
            # Monkey patch the requests library to log all requests
            old_send = requests.Session.send
            def new_send(session, request, **kwargs):
                logger.info(f"REQUEST URL: {request.url}")
                logger.info(f"REQUEST METHOD: {request.method}")
                logger.info(f"REQUEST HEADERS: {request.headers}")
                response = old_send(session, request, **kwargs)
                logger.info(f"RESPONSE STATUS: {response.status_code}")
                return response
            
            # Apply the monkey patch
            requests.Session.send = new_send
            
            # Create the chat model
            chat_model = ChatOpenAI(**model_kwargs)
            
            logger.info(f"Successfully initialized ChatOpenAI with OpenRouter: {model}")
            return chat_model
        else:
            logger.info(f"Using standard LangChain model: {model_name}")
            # Add verbose flag for standard models too
            if "verbose" not in kwargs:
                kwargs["verbose"] = True
            return langchain_init_chat_model(model_name, **kwargs)
    except Exception as e:
        logger.error(f"Error initializing chat model: {str(e)}")
        raise
