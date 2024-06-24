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
from .utils.folder import get_target_folders, init_output_folders
from typing import List


def main():
    parser = argparse.ArgumentParser(description="Process study materials and generate Anki flashcards.")
    parser.add_argument('--book_name', required=False, help="Name of the folders to process separated by comma")
    parser.add_argument('--ocr_language', default='eng', help="Language for OCR processing (default: 'eng').")

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
                # process_file(os.path.join(input_folder, file))
                log_file.write(file + '\n')
                all_processed_files.append(file)

        print(f"Updated {log_file_path} with {len(new_files)} new files.")


if __name__ == "__main__":
    main()