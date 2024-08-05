import pytesseract
from PIL import Image
import imghdr


def is_image_file(file_path: str) -> bool:
    """
    Check if a file is a valid image.

    Args:
        file_path (str): The path to the file.

    Returns:
        bool: True if the file is a valid image, False otherwise.
    """
    return imghdr.what(file_path) is not None


def get_ocr_text(image_path: str) -> str:
    """
    Perform OCR on an image file and return the extracted text.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The extracted text from the image.
    """
    if is_image_file(image_path):
        image = Image.open(image_path)
        print(image)
        text = pytesseract.image_to_string(image)
        return text
    else:
        print(f"Image file {image_path} not found or not an image")
        return ""

