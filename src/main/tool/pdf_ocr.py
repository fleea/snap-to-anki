from mistralai import Mistral, OCRResponse
from main.utils.constants import MISTRAL_API_KEY
from typing import Optional
import logging
logger = logging.getLogger(__name__)

def pdf_ocr(url: str) -> Optional[OCRResponse]:
    """If document is PDF, use this to call Mistral OCR API and return the result
    
    Args:
        url (str): URL of the PDF document
    
    Returns:
        OCRResponse: OCR response from Mistral OCR API
    """

    if not MISTRAL_API_KEY:
        logger.warning("MISTRAL_API_KEY is not set in environment variables")
        return None

    client = Mistral(api_key=MISTRAL_API_KEY)
    ocr_response = client.ocr.process(
        model="mistral-ocr-latest",
        document={
            "type": "document_url",
            "document_url": url
        }
    )
    return ocr_response