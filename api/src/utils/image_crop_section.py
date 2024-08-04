import os

import cv2


def preprocess_image(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    return img, binary


def detect_regions(binary):
    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on area
    min_area = 1000  # Adjust this value as needed
    regions = [cv2.boundingRect(c) for c in contours if cv2.contourArea(c) > min_area]

    return regions


def group_regions(regions):
    # Sort regions by y-coordinate
    sorted_regions = sorted(regions, key=lambda r: r[1])

    # Group regions by proximity
    groups = []
    current_group = [sorted_regions[0]]
    for region in sorted_regions[1:]:
        if region[1] - (current_group[-1][1] + current_group[-1][3]) < 20:  # Adjust this threshold as needed
            current_group.append(region)
        else:
            groups.append(current_group)
            current_group = [region]
    groups.append(current_group)

    return groups


def split_image(image_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    img, binary = preprocess_image(image_path)
    regions = detect_regions(binary)
    groups = group_regions(regions)

    for i, group in enumerate(groups):
        x = min(r[0] for r in group)
        y = min(r[1] for r in group)
        max_x = max(r[0] + r[2] for r in group)
        max_y = max(r[1] + r[3] for r in group)
        w = max_x - x
        h = max_y - y

        # Save the region as an image
        roi = img[y:y + h, x:x + w]
        output_path = os.path.join(output_dir, f"region_{i}.png")
        cv2.imwrite(output_path, roi)

        print(roi)
        print(f"Saved region_{i}.png to {output_path}")


if __name__ == "__main__":
    # Get the project root (3 levels up from the script location)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

    # Define paths
    input_folder = "data/input/test"
    output_folder = "data/output/test"
    image_name = "DKN06362.jpg"

    # Construct full paths
    image_path = os.path.join(project_root, input_folder, image_name)
    output_dir = os.path.join(project_root, output_folder, os.path.splitext(image_name)[0])

    print(f"Image path: {image_path}")
    print(f"Output directory: {output_dir}")

    # Call the split_image function
    split_image(image_path, output_dir)
