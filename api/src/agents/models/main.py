from langchain_openai import ChatOpenAI

from api.src.utils.constants import openai_key

model = ChatOpenAI(model="gpt-4o", temperature=0, api_key=openai_key)
