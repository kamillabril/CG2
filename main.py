from PIL import Image
from PIL import ImageColor
import pandas as pd


def create_image(size, background, foreground):
    # Create an image
    image = Image.new("RGB", size, ImageColor.getcolor(background, "RGB"))
    pixel_color = ImageColor.getcolor(foreground, "RGB")

    # Add pixels from dataset
    pixels = pd.read_csv('DS4.txt', sep=" ", header=None)
    for i in range(len(pixels)):
        current_pixel = (pixels[0][i], pixels[1][i])
        image.putpixel(current_pixel, pixel_color)

    return image


# Specify the size of the image (e.g., 540x960 pixels)
image_size = (540, 960)

# Create the image
result_image = create_image(image_size, "#556633", "#993344")

# Save the image to a file
result_image.save("picture94.png")
