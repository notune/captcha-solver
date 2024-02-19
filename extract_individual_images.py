from PIL import Image


def extract_individual_images(n, grid_path = "grid.png"):
    
    img = Image.open(grid_path)
    # Dimensions of the grid
    grid_size = (n, n)

    # Size of the individual squares (assuming each square is the same size)
    square_width = img.width // grid_size[0]
    square_height = img.height // grid_size[1]

    # Function to crop each square
    def crop_square(start_x, start_y, width, height):
        return img.crop((start_x, start_y, start_x + width, start_y + height))

    # Crop out each square and save as a new image file
    file_paths = []
    for i in range(grid_size[1]): # Row
        for j in range(grid_size[0]): # Column
            start_x = j * square_width
            start_y = i * square_height
            square_img = crop_square(start_x, start_y, square_width, square_height)
            
            # File path for the cropped image
            file_path = f'square_{i}_{j}.jpg'
            square_img.save(file_path)
            file_paths.append(file_path)
    
    return file_paths


