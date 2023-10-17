import argparse
import os
from PIL import Image
import pytesseract
from datetime import datetime


def extractThai(input_folder):
    files = os.listdir(input_folder)
    image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif"]
    image_files = [
        f for f in files if os.path.splitext(f)[1].lower() in image_extensions
    ]
    account = []
    for filename in image_files:
        image = Image.open(os.path.join(input_folder, filename))
        text = pytesseract.image_to_string(image, lang="tha+eng")
        text = text.split("\n")
        text = text[0]
        text = text.replace(" ", "")
        account.append(text)

    with open(
        os.path.join(
            ".",
            f"""{datetime.now().strftime("%Y-%m-%d_%H_%M_%S")}_extracted_result.txt""",
        ),
        "w",
        encoding="utf-8",
    ) as writer:
        writer.writelines("\n".join(account))


def main():
    try:
        parser = argparse.ArgumentParser(description="Extract thai")
        parser.add_argument(
            "--input_folder",
            "-i",
            help="Input folder containing images to extract.",
            required=True,
        )
        args = parser.parse_args()
        print(f"""{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} :: start extraction""")
        extractThai(args.input_folder)
        print(f"""{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} :: extracted""")
    except Exception as error:
        print(error)
