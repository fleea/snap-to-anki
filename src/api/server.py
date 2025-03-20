from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import AsyncIterable, List, Dict, Any
import asyncio
import json
from fastapi.responses import StreamingResponse

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import the graph from main
from src.main.graph import graph
from src.main.state import InputState as AgentInputState

class InputStateModel(BaseModel):
    image_url: str
    should_evaluate: bool = True
    export_folder: str = "/export"
    messages: List[str] = []

@app.post("/")
async def run_agent(input_state: InputStateModel):
    """Stream agent execution including node outputs"""
    # Convert Pydantic model to dict for the agent
    input_dict = {
        "image_url": input_state.image_url,
        "should_evaluate": input_state.should_evaluate,
        "export_folder": input_state.export_folder,
        "messages": input_state.messages
    }
    
    async def event_stream():
        try:
            async for event in graph.astream(input_dict):
                # Convert event to a serializable format
                serializable_event = {}
                for key, value in event.items():
                    if hasattr(value, '__dict__'):
                        # Convert custom objects to dict
                        serializable_event[key] = value.__dict__
                    elif hasattr(value, 'model_dump'):
                        # Handle Pydantic models
                        serializable_event[key] = value.model_dump()
                    else:
                        # Try to use the value directly
                        try:
                            # Test if it's JSON serializable
                            json.dumps({key: value})
                            serializable_event[key] = value
                        except (TypeError, OverflowError):
                            # If not serializable, convert to string
                            serializable_event[key] = str(value)
                
                # Convert to JSON string
                event_json = json.dumps({"event": serializable_event})
                yield f"data: {event_json}\n\n"
                await asyncio.sleep(0.1)  # Prevent overwhelming the client
        except Exception as e:
            error_json = json.dumps({"error": str(e)})
            yield f"data: {error_json}\n\n"
    
    return StreamingResponse(event_stream(), media_type="text/event-stream")