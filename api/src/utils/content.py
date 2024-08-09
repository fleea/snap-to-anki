from typing import List

from .image_file import get_data_url_from_image
from .ocr import get_ocr_text
from ..prompts.main import (
    FLASHCARD_TYPE,
    generate_prompt_from_text,
    generate_prompt_from_image,
)
from ..prompts.transcribe import transcribe_prompt


def generate_req_content(
    output_type: FLASHCARD_TYPE, local_ocr: bool = True, file_path: str = ""
) -> List[dict]:
    if local_ocr:
        ocr_text = get_ocr_text(file_path)  # THIS TAKES A WHILE
        prompt_text = generate_prompt_from_text(output_type, ocr_text)
        return [{"type": "text", "text": prompt_text}]
    else:
        prompt_text = generate_prompt_from_image(output_type)
        data_url = get_data_url_from_image(file_path)
        return [
            {"type": "text", "text": transcribe_prompt},
            {
                "type": "image_url",
                "image_url": {
                    "url": data_url,
                },
            },
        ]
