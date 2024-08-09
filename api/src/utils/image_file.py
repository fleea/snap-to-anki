import base64
import mimetypes
import os


def get_data_url_from_image(file_path: str) -> str:
    mime_type = get_mime_type(file_path)
    if mime_type is None:
        mime_type = "image/png"
    base_64_string = get_base64_string(file_path)
    return f"data:{mime_type};base64,{base_64_string}"


def get_base64_string(file_path: str) -> str:
    with open(file_path, "rb") as image_file:
        base64_bytes = base64.b64encode(image_file.read())
        base64_string = base64_bytes.decode("utf-8")
    return base64_string


def get_mime_type(file_path: str) -> str:
    """
    Extracts the MIME type from a file path.

    Args:
    file_path (str): The path to the file

    Returns:
    str: The detected MIME type, or None if not found
    """
    # Ensure mimetypes is initialized
    mimetypes.init()

    # Get the file extension
    _, extension = os.path.splitext(file_path)

    if extension:
        # Look up the MIME type
        mime_type, _ = mimetypes.guess_type(file_path)
        return mime_type
    else:
        return None


def is_valid_file(file_path):
    # List of allowed file formats
    allowed_formats = ["png", "jpeg", "gif", "webp"]

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


def get_file_name(file_path: str):
    return os.path.splitext(os.path.basename(file_path))[0]
