# Process image to be split by logical regions for further processing

import cv2
from matplotlib import pyplot as plt

import api.src.utils.constants as default_path
from api.src.utils.image.crop_and_straighten import crop_and_straighten
from api.src.utils.path import get_path


def process_image(image_path: str):
    print(f"Start processing: {image_path}")

    cropped_and_straigten = crop_and_straighten(image_path)
    print(cropped_and_straigten)
    plt.figure()
    plt.title(f'Page')
    plt.imshow(cv2.cvtColor(cropped_and_straigten, cv2.COLOR_BGR2RGB))
    plt.show()

    # CROP AND STRAIGTHEN BOOK IMAGE


if __name__ == '__main__':
    output_dir = default_path.output_dir
    folder_dir = 'test'
    img = 'DKN06527.jpg'
    input_dir = default_path.input_dir
    img_path = get_path(input_dir, folder_dir, img)
    process_image(img_path)
