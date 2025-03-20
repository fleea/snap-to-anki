from mistralai import Mistral, OCRResponse
from typing import Optional
from main.utils.constants import MISTRAL_API_KEY
import logging
logger = logging.getLogger(__name__)

def image_ocr(url: str) -> Optional[OCRResponse]:
    """Go to Mistral OCR API and return the result"""

    if not MISTRAL_API_KEY:
        logger.warning("MISTRAL_API_KEY is not set in environment variables")
        return None

    client = Mistral(api_key=MISTRAL_API_KEY)
    ocr_data = client.ocr.process(
        model="mistral-ocr-latest",
        document={
            "type": "image_url",
            "image_url": url
        }
    )
    return ocr_data