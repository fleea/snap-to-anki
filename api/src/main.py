# IMPORTANT HOW TO RUN

# via terminal
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
# import json
import os

from api.src.agents.load_transcribe.main import load_and_transcribe
from api.src.utils.csv import save_csv
from api.src.utils.folder import get_target_folders, get_processed_files
from api.src.utils.image_file import get_file_name, is_valid_file
# from snap_to_anki.ocr import process_images
# from snap_to_anki.converter import convert_images_to_anki
from api.src.utils.setup_env import setup_env


def main(folders=None, lang="auto", type="basic"):
    setup_env()

    if folders is None:
        parser = argparse.ArgumentParser(
            description="Process study materials and generate Anki flashcards."
        )
        parser.add_argument(
            "--folders",
            required=False,
            help="Name of the folders to process separated by comma",
        )
        parser.add_argument(
            "--lang",
            default="auto",
            help="Language for OCR processing (default: auto detected from the image text).",
        )
        parser.add_argument(
            "--type",
            default="basic",
            help="Anki Flashcards Type (basic, multiple-choice, cloze)",
        )

        args = parser.parse_args()
        folders = args.folders
        lang = args.lang
        type = args.type

    input_dir = "data/input"
    output_dir = "data/output"
    log_name = "processed.txt"

    target_folders = get_target_folders(input_dir, folders)
    all_processed_files = []

    for name in target_folders:
        input_folder = os.path.join(input_dir, name)
        output_folder = os.path.join(output_dir, name)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
            print(f"Directory {output_folder} created.")

        print(f"Processing Input Folder {input_folder}...")
        # List all files in the directory (flattened)
        file_list = []
        for root, _, files in os.walk(input_folder):
            for file in files:
                file_list.append(
                    os.path.relpath(os.path.join(root, file), input_folder)
                )
        print(f"Found {len(file_list)} files in {input_folder}.")
        print(f"File list: {file_list}")
        log_file_path = os.path.join(output_folder, log_name)
        processed_files = get_processed_files(log_file_path)
        print(f"File processed_files: {processed_files}")

        # Process files that are not in the log file
        new_files = [
            file
            for file in file_list
            if file not in processed_files
               and is_valid_file(os.path.join(input_folder, file))
        ]

        print(f"Found {len(new_files)} new files to process.")
        # Add new files to the processed.txt log
        with open(log_file_path, "a") as log_file:
            for file in new_files:
                print(f"Processing file: {file}")
                # START PROCESSING FILES HERE
                filename = get_file_name(file)
                file_path = os.path.join(input_folder, file)
                state = load_and_transcribe(file_path)
                print(state)

                # SAVE STATE HERE
                output_file_folder = os.path.join(output_folder, filename)
                if not os.path.exists(output_file_folder):
                    os.makedirs(output_file_folder)

                base64_file_path = os.path.join(output_file_folder, 'base_64.txt')
                with open(base64_file_path, 'w') as base64_file:
                    base64_file.write(state["base_64_string"])

                transcription_path = os.path.join(output_file_folder, 'transcription.txt')
                with open(transcription_path, 'w') as transcription_file:
                    transcription_file.write(state["transcription"])

                flashcard_path = os.path.join(output_file_folder, 'flashcard.csv')
                save_csv(state["csv"], flashcard_path)

                log_file.write(file + '\n')
                all_processed_files.append(file)

        print(f"Updated {log_file_path} with {len(new_files)} new files.")


if __name__ == "__main__":
    main()
