import pandas as pd
from io import StringIO


def save_csv(text: str, path: str):
    # Replace any escaped newlines or special characters if necessary
    content = text.replace("\\n", "\n").replace("\u00e9", "é").replace("\u00eb", "ë")

    if content.startswith("```csv"):
        content = content[len("```csv") :].strip()
    if content.startswith("```"):
        content = content[len("```") :].strip()
    if content.endswith("```"):
        content = content[: -len("```")].strip()

    print(content)
    # Use StringIO to convert the text to a file-like object
    text_io = StringIO(content)

    # Read the text into a pandas DataFrame
    df = pd.read_csv(text_io, on_bad_lines="warn")
    print(df)

    # Save the DataFrame to a CSV file
    df.to_csv(path, index=False, encoding="utf-8")
    #
    print(f"CSV file '{path}' has been written successfully.")


