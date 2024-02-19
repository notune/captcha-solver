import numpy as np
from PIL import Image

def count_transitions(arr, threshold=250):
    """
    Count transitions from non-white to white in a 1D array representing pixel intensities.
    `threshold` is used to determine what is considered white.
    """
    # Find where the pixel value is greater than the threshold (considered white)
    is_white = arr > threshold
    # Find where the transitions from non-white to white occur
    transitions = np.where(np.diff(is_white.astype(int)) == 1)[0]
    return len(transitions)

def find_image_grid_size(image_path):
    # Load the image
    image = Image.open(image_path)
    
    # Convert image to numpy array
    image_data = np.array(image)

    # Calculate the number of transitions along the x-axis (width of the image)
    num_transitions_x = count_transitions(image_data.mean(axis=0).mean(axis=1))

    # Calculate the number of transitions along the y-axis (height of the image)
    num_transitions_y = count_transitions(image_data.mean(axis=1).mean(axis=1))

    # The grid size is actually equal to the num of transitions because we have a white border in the grid image
    grid_size_x = num_transitions_x
    grid_size_y = num_transitions_y

    return grid_size_x, grid_size_y


