import pytesseract
from pytesseract import Output
import cv2


def get_largest_text(img_path):
    img = cv2.imread(img_path)
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    
    max_height = 0
    max_height_text = ""

    for i in range(len(d['text'])):
        # Extract height and text
        h = d['height'][i]
        text = d['text'][i].strip()  # Remove any leading/trailing whitespace

        # Check if current text block is taller and has valid text (not empty)
        if h > max_height and text:
            max_height = h
            max_height_text = text

    return max_height_text
