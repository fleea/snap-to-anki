from typing import List
from .base import base_template, get_columns_strings

# Specific details and instructions for multiple-choice flashcards
multiple_choice_detail = """Each flashcard should have a question with multiple answer options, including the correct answer and several incorrect but believable options.
"""

multiple_choice_instruction = """
8. Each subsequent row should contain the generated question, the four answer options, and the correct answer in the "Correct Option" column.
9. The incorrect options should be believable and, if possible, derived from the text provided. They should be plausible alternatives that could be mistakenly chosen.
10. The correct answer should be placed randomly among the four options to ensure variability.
"""


def generate_multiple_choice_prompt_text(text: str) -> str:
    return base_template.format(
        additional_detail=multiple_choice_detail,
        additional_instruction=multiple_choice_instruction,
        input_type="text input",
        flashcard_type="multiple-choice",
        columns=get_columns_strings(
            [
                "FRONT",
                "OPTION1",
                "OPTION2",
                "OPTION3",
                "OPTION4",
                "CORRECT_OPTION",
                "EXAMPLE",
                "EXTRA",
            ]
        ),
        headers='"Front";"Option1";"Option2";"Option3";"Option4";"Correct Option"',
        input_type_upper="TEXT",
        input=text,
    )


def generate_multiple_choice_prompt_image() -> str:
    return base_template.format(
        additional_detail=multiple_choice_detail,
        additional_instruction=multiple_choice_instruction,
        input_type="image from the provided URL",
        flashcard_type="multiple-choice",
        columns=get_columns_strings(
            [
                "FRONT",
                "OPTION1",
                "OPTION2",
                "OPTION3",
                "OPTION4",
                "CORRECT_OPTION",
                "EXAMPLE",
                "EXTRA",
            ]
        ),
        headers='"Front";"Option1";"Option2";"Option3";"Option4";"Correct Option"',
        input_type_upper="",
        input="",
    )
