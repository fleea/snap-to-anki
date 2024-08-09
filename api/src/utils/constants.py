# Add default paths here so it can be used by multiple files
# Not in .env because the default should be committed
import os

from dotenv import load_dotenv

# FROM ROOT DIR
input_dir = "data/input"
output_dir = "data/output"

load_dotenv()
openai_key = os.getenv("OPENAI_API_KEY")
langchain_key = os.getenv("LANGCHAIN_API_KEY")
