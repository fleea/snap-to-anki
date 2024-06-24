def get_prompt(text: str) -> str:
    prompt = f"""
        You are a highly intelligent AI capable of interpreting images and generating educational content. 
        Your task is to generate a CSV file containing Anki flashcards based on text provided below. 
        Each flashcard should have a question and an answer.
    
        Instructions:
        1. Analyze the content of the image from the provided URL.
        2. Create Anki flashcards based on the content of the image.
        3. The CSV should include four columns: "Front" (the question) and "Back" (the answer), 
        "Example"(illustrative example that clarifies the content of the flashcard, optional), 
        "Extra Notes" (clarifications, mnemonic devices, historical context to help memorize, optional)
        4. The first row must contain the headers: "Front" and "Back".
        5. Each subsequent row should contain the generated question and answer for a flashcard.
        6. Output only the CSV content without any additional text or explanations.
        7. Use ; as separator
        8. Use text language for the flashcard
    
        TEXT: {text}
        """
    return prompt
