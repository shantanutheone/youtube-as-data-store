from PIL import Image
import os
import math

def resize_image(input_path, output_path, target_size=(1920, 1080)):
    # Open the image
    img = Image.open(input_path)

    # Resize the image
    resized_img = img.resize(target_size)

    # Save the resized image to the output path
    resized_img.save(output_path)

def binary_to_images(binary_content, output_folder):
    # Define pixel colors
    black = (0, 0, 0)   # RGB values for black
    white = (255, 255, 255)  # RGB values for white
    other_color = (128, 128, 128)  # RGB values for a different color

    # Calculate the number of pixels needed for one page (1280x720)
    pixels_per_page = 1280 * 720

    # Calculate the number of pages required
    num_pages = math.ceil(len(binary_content) / pixels_per_page)

    # Iterate through each page
    for page_number in range(num_pages):
        # Calculate start and end indices for the current page
        start_index = page_number * pixels_per_page
        end_index = min((page_number + 1) * pixels_per_page, len(binary_content))

        # Create a new image with a white background
        image = Image.new('RGB', (1280, 720), white)

        # Access the pixel data of the image
        pixels = image.load()

        # Iterate through the binary content for the current page
        index = start_index
        for y in range(720):
            for x in range(1280):
                if index < end_index:
                    # Use the first bit to determine the color
                    pixel_color = black if binary_content[index] == '0' else white
                    index += 1
                else:
                    # If the binary content ends, use a different color
                    pixel_color = other_color

                # Set the pixel color
                pixels[x, y] = pixel_color

        # Save the resulting image with a sequential filename
        output_image_path = f'{output_folder}/page_{page_number + 1}.png'
        image.save(output_image_path)