from typing import List

base_template: str = """
You are a highly intelligent AI capable of interpreting images and generating educational content. 
Your task is to generate a CSV file containing Anki flashcards based on the provided input. 
{additional_detail}
Instructions:
1. Analyze the content of the {input_type}
2. Create Anki {flashcard_type} flashcards based on the content of the {input_type}.
3. Use ; as separator.
4. Use input language for the flashcard output language
5. Output only the CSV content without any additional text or explanations.
6. The CSV should include the following columns: {columns}.
7. The first row must contain the headers: {headers}.
{additional_instruction}
{input_type_upper}: {input}
"""

columns: dict[str, str] = {
    "FRONT": '"Front" (the question)',
    "FRONT_CLOZE": '"Front" (the cloze deletion sentence)',
    "BACK": '"Back" (the answer)',
    "BACK_CLOZE": '"Back" (the hidden information)',
    "EXAMPLE": '"Example" (an illustrative example that clarifies the content of the flashcard, optional)',
    "EXTRA": '"Extra Notes" (clarifications, mnemonic devices, historical context to help memorize, optional)',
    "OPTION1": '"Option1" (a possible answer)',
    "OPTION2": '"Option2" (a possible answer)',
    "OPTION3": '"Option3" (a possible answer)',
    "OPTION4": '"Option4" (a possible answer)',
    "CORRECT_OPTION": '"Correct Option" (the correct answer)',
}


def get_columns_strings(keys: List[str]) -> str:
    values = [columns[key] for key in keys if columns[key]]
    return ', '.join(values[:-1]) + ', and ' + values[-1]
