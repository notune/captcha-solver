WIP-Branch, for the captcha solver with the moondream2 model, allowing it to run on lower-end hardware.
## Description
Very basic proof-of-concept google recaptcha solver that uses the moondream2 model to extract the object name and detect the object for each square. The solver relies solely on vision, no HTML or similar.
It takes screenshots, and clicks the images at the given location. It also detects the grid size, and if new images are appearing. In my limited testing it was able to solve the captcha after a max. of 2 minutes, but is often much faster.

## Limitations
- fast gpu needed
- tested for windows 11
- only works for english captcha versions
- If images disappear, it has to re-classify all images at the end
- Only works for this specific recaptcha layout, if it changes, the reference images also have to be updated

# Installation
1. pip install protobuf PyAutoGUI opencv-python pillow transformers timm einops pytesseract 
2. Install tesseract: https://tesseract-ocr.github.io/tessdoc/Installation.html
3. Run the script `main.py` to solve a captcha, once its done it will close (the llava model should be automatically downloaded on first start)

# Contributions
Contributions welcome! If you have any issues or improvements feel free to change the code or let me know by submitting a new issue.
