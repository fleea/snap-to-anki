from enum import Enum
from .basic import generate_basic_prompt_text, generate_basic_prompt_image
from .cloze_deletion import generate_cloze_prompt_text, generate_cloze_prompt_image
from .multiple_choice import (
    generate_multiple_choice_prompt_text,
    generate_multiple_choice_prompt_image,
)

FLASHCARD_TYPE = Enum("FlashcardType", ["basic", "multiple_choice", "cloze"])


def generate_prompt_from_text(output_type: FLASHCARD_TYPE, text_content: str) -> str:
    if output_type == "cloze":
        return generate_cloze_prompt_text(text_content)
    if output_type == "multiple_choice":
        return generate_multiple_choice_prompt_text(text_content)
    else:
        return generate_basic_prompt_text(text_content)


def generate_prompt_from_image(output_type: FLASHCARD_TYPE):
    if output_type == "cloze":
        return generate_cloze_prompt_image()
    if output_type == "multiple_choice":
        return generate_multiple_choice_prompt_image()
    else:
        return generate_basic_prompt_image()
