import os
from typing import List, Optional


def list_folders(directory: str = 'data') -> List[str]:
    """
    Get a list of folder names in the specified directory.

    Args:
        directory (str): The directory to search for folders. Defaults to 'data'.

    Returns:
        List[str]: A list of folder names in the directory.
    """
    return [name for name in os.listdir(directory) if os.path.isdir(os.path.join(directory, name))]


def get_target_folders(directory: str = 'data', book_name: Optional[str] = None) -> List[str]:
    """
    Get a list of folders to process based on the book_name and directory.

    Args:
        book_name (Optional[str]): A comma-separated string of book names to search for. Defaults to None.
        directory (str): The directory to search for folders. Defaults to 'data'. No space allowed

    Returns:
        List[str]: A list of folder names to process.
    """
    if book_name is None:
        return list_folders(directory)

    folders = []
    for name in book_name.split(','):
        # Check if folder exists
        if os.path.isdir(os.path.join(directory, name)):
            folders.append(name)

    return folders


def get_file_name(file_path: str):
    return os.path.splitext(os.path.basename(file_path))[0]


def get_processed_files(log_file_path: str) -> List[str]:
    # Read the existing log file if it exists
    # Use set to avoid duplicates
    processed_files = set()
    if os.path.exists(log_file_path):
        with open(log_file_path, 'r') as log_file:
            processed_files = set(log_file.read().splitlines())
    return processed_files


def get_all_file_names_in_folder(input_folder: str) -> List[str]:
    # List all files in the directory (flattened)
    file_list = []
    for root, _, files in os.walk(input_folder):
        for file in files:
            file_list.append(os.path.relpath(os.path.join(root, file), input_folder))
    return file_list


def is_valid_file(file_path):
    # List of allowed file formats
    allowed_formats = ['png', 'jpeg', 'gif', 'webp']

    # Check if the file exists
    if not os.path.exists(file_path):
        return False

    # Get the file size in MB
    file_size = os.path.getsize(file_path) / (1024 * 1024)

    # Get the file extension (without the dot) and convert to lowercase
    file_extension = os.path.splitext(file_path)[1][1:].lower()

    # Check if the file meets all criteria
    if file_size < 20 and file_extension in allowed_formats:
        return True
    else:
        return False
