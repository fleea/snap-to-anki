import logging
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
    
    # Get evaluation state variables if they exist, otherwise use defaults
    evaluation_retry_count = getattr(state, 'evaluation_retry_count', 0)
    
    # Default should_evaluate to True if not specified
    should_evaluate = getattr(state, 'should_evaluate', True)
    
    if not should_evaluate:
        return {
            "csv": state.csv,
            "analysis_output": state.analysis_output,
            "passed_evaluation": True
        }
    
    if evaluation_retry_count >= EVALUATOR_MAX_RETRY:
        logging.warning(f"Reached maximum evaluation retry count ({EVALUATOR_MAX_RETRY}). Proceeding to exporter.")
        return {
            "csv": state.csv,
            "analysis_output": state.analysis_output,
            "passed_evaluation": False
        }
    
    model = init_chat_model(EVALUATOR_MODEL, temperature=EVALUATOR_TEMPERATURE)
    
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(
            content=[
                {
                    "type": "text",
                    "text": f"""
                        Please evaluate the following flashcards generated from an image.
                        
                        Image URL: {state.image_url}
                        
                        Content Analysis Results:
                        {state.analysis_output.model_dump_json(indent=2)}
                        
                        Generated CSV Content:
                        ```
                        {state.csv}
                        ```
                        
                        Evaluate the flashcards based on the criteria in your instructions.
                        Provide a structured response with your evaluation and the next step.
                    """,
                }
            ]
        ),
    ]
    
    evaluation_response = await model.ainvoke(messages, config)
    evaluation_text = evaluation_response.content
    
    passed_evaluation = "valid" in evaluation_text.lower() and not ("invalid" in evaluation_text.lower())
    
    evaluation_result = EvaluationResult(
        feedback=evaluation_text,
        next_step="exporter" if passed_evaluation else "writer"
    )
    
    evaluation_retry_count = getattr(state, 'evaluation_retry_count', 0) + 1
    
    return {
        "csv": state.csv,
        "analysis_output": state.analysis_output,
        "evaluation_result": evaluation_result,
        "passed_evaluation": passed_evaluation,
        "evaluation_retry_count": evaluation_retry_count
    }
