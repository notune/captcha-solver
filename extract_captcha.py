import cv2

# Function to perform template matching and return the match position and value
def template_match(big_img_gray, template_gray, method=cv2.TM_CCOEFF_NORMED):
    # Apply template matching with the given method
    res = cv2.matchTemplate(big_img_gray, template_gray, method)
    # Find the location with the highest match
    _, max_val, _, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + template_gray.shape[1], top_left[1] + template_gray.shape[0])
    
    return top_left, bottom_right, max_val

def extract_captcha(big_image_path = 'big_image.png', part1_bottom_path = 'part1_bottom.png', part2_top_path = 'part2_top.png'):
    # Load the big image and convert it to grayscale
    big_image = cv2.imread(big_image_path, cv2.IMREAD_COLOR)
    big_image_gray = cv2.cvtColor(big_image, cv2.COLOR_BGR2GRAY)

    #convert top and bottom part to grayscale
    part1_bottom = cv2.imread(part1_bottom_path, cv2.IMREAD_COLOR)
    part2_top = cv2.imread(part2_top_path, cv2.IMREAD_COLOR)
    part1_bottom_gray = cv2.cvtColor(part1_bottom, cv2.COLOR_BGR2GRAY)
    part2_top_gray = cv2.cvtColor(part2_top, cv2.COLOR_BGR2GRAY)

    # Perform template matching for the top and bottom parts
    top_match_top_left, _, top_match_val = template_match(big_image_gray, part2_top_gray)
    bottom_match_top_left, bottom_match_bottom_right, bottom_match_val = template_match(big_image_gray, part1_bottom_gray)

    # Validate the match by checking if the bottom is below the top, and the matches are good
    if (top_match_val > 0.95) and (bottom_match_val > 0.95) and (bottom_match_top_left[1] > top_match_top_left[1]):
        # If valid, extract the area between the top and bottom matches
        extracted_area = big_image[top_match_top_left[1]:bottom_match_bottom_right[1], top_match_top_left[0]:bottom_match_bottom_right[0]]

        # Save the extracted area to a file
        extracted_img_path = 'extracted_image.png'
        cv2.imwrite(extracted_img_path, extracted_area)
        return True
    else:
        return False
