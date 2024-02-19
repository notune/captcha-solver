
def extract_captcha_grid(final_path='grid.png'):
    import cv2

    extracted_image = cv2.imread('extracted_image.png', cv2.IMREAD_COLOR)

    # Crop the image starting at 124px to 517px height, and remove 3px from left and right in width
    cropped_final_image = extracted_image[124:517, 3:-3]

    # Save the final cropped image to a new file
    cv2.imwrite(final_path, cropped_final_image)

