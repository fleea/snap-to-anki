import os

from api.src.utils.constants import openai_key, langchain_key


def setup_env():
    os.environ["OPENAI_API_KEY"] = openai_key

    # OPTIONAL
    os.environ["LANGSMITH_TRACING"] = "false"
    os.environ["LANGSMITH_API_KEY"] = langchain_key
