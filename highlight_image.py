from PIL import Image, ImageDraw

def highlight_in_grid(col, row):
    # Load the image
    img = Image.open("grid.png")

    # Since we have a 4x4 grid, each cell's width and height can be determined by dividing
    # the total width and height of the image by 4
    cell_width = img.width // 4
    cell_height = img.height // 4

    top_left_x = col * cell_width
    top_left_y = row * cell_height

    # Now we create a draw object to add a border
    draw = ImageDraw.Draw(img)

    # We'll draw a rectangle around the 6th image.
    # Since we want a 3 pixel thick border, we define the rectangle to cover the edge of the image
    # and extend 3 pixels beyond it.
    draw.rectangle(
        [top_left_x, top_left_y, top_left_x + cell_width, top_left_y + cell_height],
        outline="red",
        width=3
    )

    # Save the result
    bordered_image_path = "grid_with_border.png"
    img.save(bordered_image_path)

    return bordered_image_path
