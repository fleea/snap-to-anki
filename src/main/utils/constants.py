"""
Constants module for centralized configuration management.
This file defines default values for configuration constants and loads overrides from environment variables.
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Helper function to get environment variable with default
def get_env(key, default):
    """Get environment variable value or return default if not set"""
    value = os.getenv(key)
    return value if value is not None else default

# OpenRouter base URL
OPENROUTER_BASE_URL = get_env("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

# Content Analysis configuration
CONTENT_ANALYSIS_MODEL = get_env("CONTENT_ANALYSIS_MODEL", "openai:gpt-4o")
CONTENT_ANALYSIS_TEMPERATURE = float(get_env("CONTENT_ANALYSIS_TEMPERATURE", "0.8"))

# Flashcard Writer configuration
FLASHCARD_WRITER_MODEL = get_env("FLASHCARD_WRITER_MODEL", "openrouter:google/gemma-3-27b-it")
FLASHCARD_WRITER_TEMPERATURE = float(get_env("FLASHCARD_WRITER_TEMPERATURE", "0.8"))

# Evaluator configuration
EVALUATOR_MODEL = get_env("EVALUATOR_MODEL", "openai:gpt-4o")
EVALUATOR_TEMPERATURE = float(get_env("EVALUATOR_TEMPERATURE", "0.2"))
EVALUATOR_MAX_RETRY = int(get_env("EVALUATOR_MAX_RETRY", "2"))

# Node names
# Used in edge routing
CONTENT_ANALYSIS_NODE = "content_analysis"
FLASHCARD_WRITER_NODE = "flashcard_writer"
FLASHCARD_EVALUATOR_NODE = "flashcard_evaluator"
FLASHCARD_EXPORTER_NODE = "flashcard_exporter"
