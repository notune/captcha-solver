import cv2
import numpy as np


def is_significantly_different(image_path1, image_path2, threshold):
    # Load the images
    image1 = cv2.imread(image_path1)
    image2 = cv2.imread(image_path2)

    # Convert images to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Compute the absolute difference between the images
    diff = cv2.absdiff(gray1, gray2)

    # Threshold the difference
    _, thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Calculate the percentage of different pixels
    non_zero_count = np.count_nonzero(thresh)
    total_pixels = thresh.size
    difference_percentage = (non_zero_count / total_pixels) * 100

    # Check if the difference is above the threshold
    return difference_percentage > threshold