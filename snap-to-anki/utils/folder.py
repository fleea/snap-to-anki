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


