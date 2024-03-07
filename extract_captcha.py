import cv2
import numpy as np

def extract_and_save_captcha(image_before_click_path, image_after_click_path):
    def get_contours_with_expected_size(contours, expected_width, expected_height, tolerance=0.15):
        # Find contours that match the expected size within a certain tolerance
        possible_contours = []
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if (1 - tolerance) * expected_width < w < (1 + tolerance) * expected_width and \
               (1 - tolerance) * expected_height < h < (1 + tolerance) * expected_height:
                possible_contours.append(contour)
        return possible_contours

    # Load the images
    before_click = cv2.imread(image_before_click_path)
    after_click = cv2.imread(image_after_click_path)

    # Convert the images to grayscale
    before_gray = cv2.cvtColor(before_click, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(after_click, cv2.COLOR_BGR2GRAY)

    # Compute the absolute difference between the images
    difference = cv2.absdiff(before_gray, after_gray)

    # Threshold the difference
    _, thresh = cv2.threshold(difference, 30, 255, cv2.THRESH_BINARY)

    # Find the contours from the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Now, find possible contours
    possible_contours = get_contours_with_expected_size(contours, 401, 580)

    # If multiple contours are found, we'll use the one closest to the expected size
    if possible_contours:
        closest_contour = min(possible_contours, key=lambda c: abs(cv2.contourArea(c) - 401 * 580))
        x, y, w, h = cv2.boundingRect(closest_contour)

        # Crop the after_click image based on the bounding rectangle of the closest contour
        ui_element_corrected = after_click[y:y+h, x:x+w]

        # Save the new cropped UI element image
        ui_element_corrected_path = 'extracted_image.png'
        cv2.imwrite(ui_element_corrected_path, ui_element_corrected)
        return True
    else:
        print("No UI element with the expected size was found.")
        return False
