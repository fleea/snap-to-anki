# BASIC FLASHCARDS
# Basic (Front and Back):
# Question: A prompt or question on the front of the card.
# Answer: The answer on the back of the card.
# Example:
# Front: "Capital of France?"
# Back: "Paris"
from .base import base_template, get_columns_strings


def generate_basic_prompt_text(text: str) -> str:
    return base_template.format(
        additional_detail="Each flashcard should have a question and an answer.",
        additional_instruction="8. Each subsequent row should contain the generated question and answer for a flashcard.",
        input_type="text input",
        flashcard_type="basic",
        columns=get_columns_strings(["FRONT", "BACK", "EXAMPLE", "EXTRA"]),
        headers='''"Front" and "Back"''',
        input_type_upper="TEXT",
        input=text
    )


def generate_basic_prompt_image() -> str:
    return base_template.format(
        additional_detail="Each flashcard should have a question and an answer.",
        additional_instruction="8. Each subsequent row should contain the generated question and answer for a flashcard.",
        input_type="image from the provided URL",
        flashcard_type="basic",
        columns=get_columns_strings(["FRONT", "BACK", "EXAMPLE", "EXTRA"]),
        headers='''"Front" and "Back"''',
        input_type_upper="",
        input=""
    )


if __name__ == "__main__":
    print(generate_basic_prompt_image())
    print(generate_basic_prompt_text("input text"))
