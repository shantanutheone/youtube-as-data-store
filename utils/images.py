from PIL import Image
import os

def resize_image(input_path, output_path, target_size=(1920, 1080)):
    # Open the image
    img = Image.open(input_path)

    # Resize the image
    resized_img = img.resize(target_size)

    # Save the resized image to the output path
    resized_img.save(output_path)

# Example usage:
# input_folder = "path/to/original/images"
# output_folder = "path/to/resized/images"
# resize_images(input_folder, output_folder)