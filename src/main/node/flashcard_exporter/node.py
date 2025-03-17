import os
import logging
from typing import Dict, Any
from langchain_core.runnables import RunnableConfig
from .state import FlashcardExporterState


async def flashcard_exporter(
    state: FlashcardExporterState, config: RunnableConfig
) -> Dict[str, Any]:
    """Export flashcard CSV content to a file in the export directory"""
    
    title = state.analysis_output.title
    csv_content = state.csv
    export_folder = getattr(state, 'export_folder', '/export')
    
    if not export_folder or export_folder.strip() == "":
        return {
            "status": "skipped",
            "message": "Export skipped because export_folder is not specified"
        }
    
    # Always use /export as the base directory and then add the specified folder inside it
    # Remove leading slash if present
    if export_folder.startswith("/"):
        export_folder = export_folder[1:]
    
    # Create path with /export as the base directory
    export_dir = os.path.join(os.getcwd(), "export", export_folder)
    os.makedirs(export_dir, exist_ok=True)
    
    filename = f"{title}.csv"
    filepath = os.path.join(export_dir, filename)
    
    try:
        if csv_content is None:
            raise ValueError("CSV content is None")
        
        if not isinstance(csv_content, str):
            csv_content = str(csv_content)
        
        csv_content = csv_content.replace('\\n', '\n')
        
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
