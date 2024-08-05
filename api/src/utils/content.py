from typing import List
from .ocr import get_ocr_text
from ..prompts.main import FLASHCARD_TYPE, generate_prompt_from_text, generate_prompt_from_image
import base64


def get_base64_string(file_path: str) -> str:
    with open(file_path, "rb") as image_file:
        base64_bytes = base64.b64encode(image_file.read())
        base64_string = base64_bytes.decode('utf-8')
    return base64_string


def generate_req_content(output_type: FLASHCARD_TYPE, local_ocr: bool = True, file_path: str = "") -> List[dict]:
    if local_ocr:
        ocr_text = get_ocr_text(file_path)  # THIS TAKES A WHILE
        prompt_text = generate_prompt_from_text(output_type, ocr_text)
        return [{"type": "text", "text": prompt_text}]
    else:
        base64_string = get_base64_string(file_path)
        prompt_text = generate_prompt_from_image(output_type)
        return [
            {"type": "text", "text": prompt_text},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_string}",
                },
            },
        ]
