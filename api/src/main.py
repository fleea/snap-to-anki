# IMPORTANT HOW TO RUN
# export PYTHONPATH=$PYTHONPATH:.
# python3.12 api/src/main.py --folders test
# Check input files in data/folder
# For each folder, check corresponding output/folder
# If no corresponding folder, run the script for all images in the folder
# If there is corresponding folder, check processed.txt in that folder
# If there is no processed.txt in the folder, run ocr to all
# If there is no line in processed.txt that is corresponding to the file name in data/book-name folder,
# then process and save

# Image requirements
# Error: 400, {
#   "error": {
#     "message": "You uploaded an unsupported image. Please make sure your image is below 20 MB in size and is of one the following formats: ['png', 'jpeg', 'gif', 'webp'].",
#     "type": "invalid_request_error",
#     "param": null,
#     "code": "invalid_image_format"
#   }
# }

import argparse
import json
import os

from dotenv import load_dotenv

from api.src.utils.content import generate_req_content
from api.src.utils.csv import save_csv
# from snap_to_anki.ocr import process_images
# from snap_to_anki.converter import convert_images_to_anki
from api.src.utils.folder import get_target_folders, get_file_name, get_processed_files, is_valid_file
from api.src.utils.openai import get_anki_csv

load_dotenv()
openai_key = os.getenv('OPENAI_API_KEY')


def main():
    parser = argparse.ArgumentParser(description="Process study materials and generate Anki flashcards.")
    parser.add_argument('--folders', required=False, help="Name of the folders to process separated by comma")
    parser.add_argument('--lang', default='auto', help="Language for OCR processing (default: 'eng').")
    parser.add_argument('--local_ocr', action='store_true',
                        help="Use Local OCR (for books with text only) to save cost")
    parser.add_argument('--type', default='basic', help="Anki Flashcards Type (basic, multiple-choice, cloze)")

    args = parser.parse_args()
    folders = args.folders
    input_dir = 'data/input'
    output_dir = 'data/output'
    log_name = 'processed.txt'
    anki_type = args.type
    local_ocr = args.local_ocr

    target_folders = get_target_folders(input_dir, folders)
    print(target_folders)
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
        processed_files = get_processed_files(log_file_path)

        # Process files that are not in the log file
        new_files = [
            file for file in file_list
            if file not in processed_files and is_valid_file(os.path.join(input_folder, file))
        ]

        # Add new files to the processed.txt log
        with open(log_file_path, 'a') as log_file:
            for file in new_files:
                # START PROCESSING FILES HERE
                filename = get_file_name(file)
                file_path = os.path.join(input_folder, file)
                print(file_path)
                prompt_content = generate_req_content(anki_type, local_ocr, file_path)
                print(prompt_content)

                # OCR RESULT
                # ocr_file_path = os.path.join(output_folder, filename + '-ocr.txt')
                # with open(ocr_file_path, 'w') as ocr_file:
                #     ocr_file.write(ocr_text)

                # RESPONSE RESULT (from chatgpt)
                response = get_anki_csv(openai_key, prompt_content)  # THIS IS EXPENSIVE
                response_file_path = os.path.join(output_folder, filename + '-response.json')
                with open(response_file_path, 'w') as csv_file:
                    json.dump(response, csv_file)

                csv_file_path = os.path.join(output_folder, filename + '-flashcard.csv')
                print(response)
                content = response["choices"][0]["message"]["content"]

                save_csv(content, csv_file_path)

                log_file.write(file + '\n')
                all_processed_files.append(file)

        print(f"Updated {log_file_path} with {len(new_files)} new files.")


if __name__ == "__main__":
    main()
