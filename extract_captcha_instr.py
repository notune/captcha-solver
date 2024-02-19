
def extract_captcha_instr():
    import cv2
    # Load the previously extracted image
    extracted_img_path = 'extracted_image.png'
    extracted_image = cv2.imread(extracted_img_path, cv2.IMREAD_COLOR)

    # Crop the top 124 pixels from the extracted image
    cropped_image = extracted_image[:124, :]

    # Save the cropped image to a new file
    cropped_img_path = 'instr.png'
    cv2.imwrite(cropped_img_path, cropped_image)
