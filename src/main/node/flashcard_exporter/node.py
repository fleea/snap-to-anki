import os
import logging
from typing import Dict, Any
from langchain_core.runnables import RunnableConfig
from .state import FlashcardExporterState


async def flashcard_exporter(
    state: FlashcardExporterState, config: RunnableConfig
) -> Dict[str, Any]:
    """Export flashcard CSV content to a file in the export directory"""
    
    # Get the title from content analysis output and the CSV content
    title = state.analysis_output.title
    csv_content = state.csv
    
    # Create the export directory if it doesn't exist
    export_dir = os.path.join(os.getcwd(), "export")
    os.makedirs(export_dir, exist_ok=True)
    
    # Create a filename using the title
    filename = f"{title}.csv"
    filepath = os.path.join(export_dir, filename)
    
    try:
        # Ensure csv_content is a string
        if csv_content is None:
            raise ValueError("CSV content is None")
        
        # Convert to string if it's not already
        if not isinstance(csv_content, str):
            csv_content = str(csv_content)
        
        # Fix any escaped newlines by replacing them with actual newlines
        # This handles cases where the model outputs "\n" as a literal string
        csv_content = csv_content.replace('\\n', '\n')
        
        # Write the CSV content to the file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(csv_content)
        
        logging.info(f"Successfully exported flashcards to {filepath}")
        
        return {
            "status": "success",
            "message": f"Flashcards exported to {filepath}",
            "filepath": filepath
        }
    
    except Exception as e:
        error_msg = f"Error exporting flashcards: {str(e)}"
        logging.error(error_msg)
        
        return {
            "status": "error",
            "message": error_msg
        }
