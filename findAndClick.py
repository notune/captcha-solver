import cv2
import numpy as np
import pyautogui
import random

def findAndClick(reference_image_path, max_offset, special_offset=None):

    # Load the reference image
    reference_image = cv2.imread(reference_image_path, cv2.IMREAD_COLOR)

    # Ensure the reference image is in the correct format
    if reference_image is None:
        raise Exception("Reference image not found or format is not supported")

    # Convert the reference image to 3 channels if it's not
    if reference_image.shape[2] == 4:
        reference_image = cv2.cvtColor(reference_image, cv2.COLOR_BGRA2BGR)

    # Take a screenshot
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Find the reference image in the screenshot
    result = cv2.matchTemplate(screenshot, reference_image, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    print(f'findAndClick max_val: {max_val}')

    if max_val > 0.95:
        center_x = max_loc[0] + reference_image.shape[1] // 2
        center_y = max_loc[1] + reference_image.shape[0] // 2

        # Generate random offset within specified range
        offset_x = random.randint(-max_offset, max_offset)
        offset_y = random.randint(-max_offset, max_offset)

        # Apply offset to the center coordinates
        click_x = center_x + offset_x
        click_y = center_y + offset_y

        if special_offset:
            click_x += special_offset[0]
            click_y += special_offset[1]

        pyautogui.click(click_x, click_y)
        return True
    else:
        return False
