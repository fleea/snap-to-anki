import logging
import json
import re
from typing import Dict, Any, Literal
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from .state import FlashcardEvaluatorState, EvaluationResult
from .prompt import SYSTEM_PROMPT
from main.utils.chat_models import init_chat_model
from main.utils.constants import EVALUATOR_MODEL, EVALUATOR_TEMPERATURE, EVALUATOR_MAX_RETRY

async def flashcard_evaluator(
    state: FlashcardEvaluatorState, config: RunnableConfig
) -> Dict[str, Any]:
    """Evaluate the quality and correctness of generated flashcards"""
    
    # Get retry count if it exists, otherwise use default
    evaluation_retry_count = getattr(state, 'evaluation_retry_count', 0)
    
    model = init_chat_model(EVALUATOR_MODEL, temperature=EVALUATOR_TEMPERATURE).with_structured_output(EvaluationResult)
    
    # Format the input according to the new prompt template
    transcription_text = f"Transcription: {state.analysis_output.model_dump_json(indent=2)}"
    flashcard_text = f"Flashcard: \n```\n{state.csv}\n```"
    prompt = SYSTEM_PROMPT.format(
        transcription=transcription_text,
        flashcard=flashcard_text
    )
    
    messages = [
        SystemMessage(content=prompt),
        HumanMessage(
            content=[
                {
                    "type": "text",
                    "text": "Please evaluate the flashcards based on the criteria in your instructions."
                },
                { "type": "image_url", "image_url": {"url":state.image_url}}
            ]
        )
    ]
    
    # Use structured output to directly get the evaluation result
    evaluation_result = await model.ainvoke(messages, config)
    
    # Increment retry count
    evaluation_retry_count += 1
    
    return {
        "csv": state.csv,
        "analysis_output": state.analysis_output,
        "evaluation_result": evaluation_result,
        "evaluation_retry_count": evaluation_retry_count
    }
