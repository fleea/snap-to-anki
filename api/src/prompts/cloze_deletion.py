# Cloze Deletion: This type hides specific parts of the text, allowing you to test your recall for specific information within a larger context.
# Question: A sentence or paragraph with certain words removed (e.g., "The capital of France is {{c1::Paris}}.")
# Answer: The missing word or phrase.
# Example:
# Front: "The capital of France is {{c1::Paris}}."
# Back: "Paris"
from .base import base_template, get_columns_strings


cloze_detail = """Each flashcard should have a sentence with specific information removed for the user to recall, 
using the cloze deletion format with double brackets.
"""

cloze_intruction = """
8. Each subsequent row should contain the generated cloze deletion sentence and the hidden information for a flashcard.
9. Use the cloze deletion format {{c1::Text-to-be-hidden}} for the first cloze deletion in each sentence. 
For additional deletions in the same sentence, increment the number (e.g., {{c2::Text-to-be-hidden}})
10. The "Front" column should contain the sentence with the cloze deletion format applied.
11. The "Back" column should contain the text that was hidden within the cloze deletion brackets.
"""


def generate_cloze_prompt_text(text: str) -> str:
    return base_template.format(
        additional_detail={cloze_detail},
        additional_instructions={cloze_intruction},
        input_type="text input",
        flashcard_type="basic",
        columns=get_columns_strings(["FRONT_CLOZE", "BACK_CLOZE", "EXAMPLE", "EXTRA"]),
        headers='''"Front" and "Back"''',
        input_type_upper="TEXT",
        input=text,
    )


def generate_cloze_prompt_image() -> str:
    return base_template.format(
        additional_detail={cloze_detail},
        additional_instructions={cloze_intruction},
        input_type="image from the provided URL",
        flashcard_type="basic",
        columns=get_columns_strings(["FRONT_CLOZE", "BACK_CLOZE", "EXAMPLE", "EXTRA"]),
        headers='''"Front" and "Back"''',
        input_type_upper="",
        input="",
    )
