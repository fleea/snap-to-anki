# Snap-to-Anki

Snap-to-Anki is a tool that converts screenshots of study materials into Anki-compatible flashcards. By leveraging advanced OCR and LLM technologies, Snap-to-Anki streamlines the creation of effective, personalized study aids. The project also aims to reduce LLM API costs by performing OCR offline, making it both efficient and cost-effective.

## Features

- **Text Extraction from Images**: Automatically extracts text from images using Optical Character Recognition (OCR).
- **Question and Answer Generation**: Generates comprehensive questions and answers from raw text using Large Language Models (LLMs).
- **Cloze Deletion Creation**: Creates fill-in-the-blank (cloze) flashcards for key information.
- **Summarization**: Summarizes complex content into concise flashcard entries.
- **Image Annotation**: Annotates and creates image occlusion flashcards from diagrams and charts.
- **CSV Formatting for Anki**: Formats extracted and generated content into CSV files ready for Anki import.
- **Cost Efficiency**: Reduces LLM API costs by performing OCR offline.

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/fleea/snap-to-anki.git
    cd snap-to-anki
    ```

2. **Install required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Ensure Tesseract OCR is installed:**
    - For Windows: Download and install from [here](https://github.com/UB-Mannheim/tesseract/wiki).
    - For Mac: Install using Homebrew:
      ```sh
      brew install tesseract
      ```
    - For Linux: Install using package manager:
      ```sh
      sudo apt-get install tesseract-ocr
      ```

4. **Add your OpenAI API token:**
    - Create a `.env` file in the root directory of the project.
    - Add your OpenAI API token to the `.env` file:
      ```sh
      OPENAI_API_KEY=your_openai_api_key_here
      ```

## Usage

1. **Prepare your images and study material:**
    - Place your textbook screenshots or images in the `snap_to_anki/data/input_images` directory.

2. **Run the conversion script:**
    ```sh
    python -m snap_to_anki.converter
    ```

3. **Import the generated CSV file into Anki:**
    - Open Anki.
    - Go to `File` > `Import`.
    - Select the `snap_to_anki/data/output/anki_flashcards.csv` file.
    - Map the fields correctly and import.


## Example

### Input Image
Place your screenshot in the `snap_to_anki/data/input_images` folder. For example, `photosynthesis.png`.

### Generated Flashcard
The tool will generate entries such as:

| Front                                       | Back                                                                 |
|---------------------------------------------|----------------------------------------------------------------------|
| What is photosynthesis?                     | Photosynthesis is the process by which green plants use sunlight...  |
| The capital of France is {{c1::Paris}}.     | The capital of France is Paris.                                      |
| Identify this molecule. <img src='glucose.png'> | It's glucose.                                                        |

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [OpenAI](https://openai.com/)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Anki](https://apps.ankiweb.net/)

## Contact

For questions or suggestions, please open an issue.

---

Happy Studying!