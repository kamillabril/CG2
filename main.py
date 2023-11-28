from PIL import Image
import pandas as pd

def create_image(size):
    # Create an image
    image = Image.new("RGB", size, (231, 255, 149))

    # Add pixels from dataset
    X = pd.read_csv('DS4.txt', sep=" ", header=None)
    for i in range(22981):
        current_pixel = (X[0][i], X[1][i])
        image.putpixel(current_pixel, (100, 100, 255))

    return image

# Specify the size of the image (e.g., 540x960 pixels)
image_size = (540, 960)

# Create the image
result_image = create_image(image_size)

# Save the image to a file
result_image.save("picture94.png")