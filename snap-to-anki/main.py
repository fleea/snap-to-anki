# Check input files in data/folder
# For each folder, check corresponding output/folder
# If no corresponding folder, run the script for all images in the folder
# If there is corresponding folder, check processed.txt in that folder
# If there is no processed.txt in the folder, run ocr to all
# If there is no line in processed.txt that is corresponding to the file name in data/book-name folder,
# then process and save

import os
import argparse
# from snap_to_anki.ocr import process_images
# from snap_to_anki.converter import convert_images_to_anki
from .utils.folder import get_target_folders, get_file_name
from typing import List
from .utils.ocr import process_image
from dotenv import load_dotenv
from .utils.prompt import get_prompt
from .utils.openai import get_anki_csv
from .utils.csv import save_csv
import json

load_dotenv()
openai_key = os.getenv('OPENAI_API_KEY')


def main():
    parser = argparse.ArgumentParser(description="Process study materials and generate Anki flashcards.")
    parser.add_argument('--book_name', required=False, help="Name of the folders to process separated by comma")
    parser.add_argument('--ocr_language', default='eng', help="Language for OCR processing (default: 'eng').")
    parser.add_argument('--local-ocr', default=False, help="Use Local OCR (for books with text only) to save cost")

    args = parser.parse_args()
    book_names = args.book_name
    input_dir = 'data'
    output_dir = 'output'
    log_name = 'processed.txt'

    target_folders = get_target_folders(input_dir, book_names)
    all_processed_files = []

    for name in target_folders:
        input_folder = os.path.join(input_dir, name)
        output_folder = os.path.join(output_dir, name)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            print(f"Directory {output_folder} created.")

        # List all files in the directory (flattened)
        file_list = []
        for root, _, files in os.walk(input_folder):
            for file in files:
                file_list.append(os.path.relpath(os.path.join(root, file), input_folder))

        log_file_path = os.path.join(output_folder, log_name)

        # Read the existing log file if it exists
        # Use set to avoid duplicates
        processed_files = set()
        if os.path.exists(log_file_path):
            with open(log_file_path, 'r') as log_file:
                processed_files = set(log_file.read().splitlines())

        # Process files that are not in the log file
        new_files = [file for file in file_list if file not in processed_files]

        # Add new files to the processed.txt log
        with open(log_file_path, 'a') as log_file:
            for file in new_files:
                # START PROCESSING FILES HERE
                print(os.path.join(input_folder, file))
                ocr_text = process_image(os.path.join(input_folder, file))  # THIS TAKES A WHILE
                prompt_text = get_prompt(ocr_text)
                filename = get_file_name(file)
                print(filename, prompt_text)

                # OCR RESULT
                ocr_file_path = os.path.join(output_folder, filename + '-ocr.txt')
                with open(ocr_file_path, 'w') as ocr_file:
                    ocr_file.write(ocr_text)

                # RESPONSE RESULT (from chatgpt)
                response = get_anki_csv(openai_key, prompt_text)  # THIS IS EXPENSIVE
                response_file_path = os.path.join(output_folder, filename + '-response.json')
                with open(response_file_path, 'w') as csv_file:
                    json.dump(response, csv_file)

                csv_file_path = os.path.join(output_folder, filename + '-flashcard.csv')
                content = response["choices"][0]["message"]["content"]

                save_csv(content, csv_file_path)

                log_file.write(file + '\n')
                all_processed_files.append(file)

        print(f"Updated {log_file_path} with {len(new_files)} new files.")


if __name__ == "__main__":
    main()
