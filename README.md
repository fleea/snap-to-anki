# Snap-to-Anki API

This project is an API for converting images of study materials into Anki flashcards.

## Prerequisites

- Python 3.12
- pip (Python package manager)

## Setup

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-name>
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python3.12 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r api/requirements.txt
   ```

4. Set up environment variables:
   Create a `.env` file in the root directory with the following content:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   LANGCHAIN_API_KEY=your_langchain_api_key_here # Optional
   ```
   Replace `your_openai_api_key_here` and `your_langchain_api_key_here` with your actual API keys.

## Running the Application

1. Ensure you're in the project root directory and your virtual environment is activated.

2. Set the PYTHONPATH:
   ```
   export PYTHONPATH=$PYTHONPATH:.
   ```

3. Run the main script:
   ```
   python3.12 api/src/main.py --folders test
   ```
   Replace `test` with the name of the folder(s) you want to process. You can specify multiple folders by separating
   them with commas.

4. The script will process the images in the specified folder(s) and generate Anki flashcards in CSV format.

## Folder Structure

- `api`: Contains the source code for the API.
- `data`: Contains the input and output folders.
    - `data/input`: Place your input images in subfolders here.
    - `data/output`: The generated flashcards and other output files will be saved here.

### Example input and output folder structure:

- `data/input`
    - `book_name`
        - `image1.png`
        - `image2.jpg`
- `data/output`
    - `book_name`
        - `image1`
            - `base64.txt`
            - `transcription.txt`
            - `flashcard.csv`
        - `image2`
            - `base64.txt`
            - `transcription.txt`
            - `flashcard.csv`

## Additional Notes

- The application uses OpenAI's GPT-4 model for text generation. Ensure you have sufficient credits in your OpenAI
  account.
- For each processed image, the application generates a base64 encoding, a transcription, and a CSV file with
  flashcards.

## Troubleshooting

If you encounter any issues:

1. Ensure all dependencies are correctly installed.
2. Check that your API keys are correctly set in the `.env` file.
3. Verify that the input images are in a supported format (png, jpeg, gif, webp) and under 20MB in size.

For more detailed information about the code structure and functionality, please refer to the individual Python files in
the `api/src` directory.