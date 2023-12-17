from PIL import Image
import os
import math

def binary_to_images(binary_content, output_folder):
    # Define pixel colors
    black = (0, 0, 0)   # RGB values for black
    white = (255, 255, 255)  # RGB values for white
    other_color = (128, 128, 128)  # RGB values for a different color

    # Calculate the number of pixels needed for one page (1280x720)
    pixels_per_page = 1280 * 720

    # Define the resolution for a single bit (8x8 pixels)
    resolution = 8

    # Calculate the number of bits that can fit in one page
    bits_per_page = pixels_per_page // (resolution ** 2)

    # Calculate the number of pages required
    num_pages = math.ceil(len(binary_content) / bits_per_page)

    # Iterate through each page
    for page_number in range(num_pages):
        # Calculate start and end indices for the current page
        start_index = page_number * bits_per_page
        end_index = min((page_number + 1) * bits_per_page, len(binary_content))

        # Create a new image with a white background
        image = Image.new('RGB', (1280, 720), white)

        # Access the pixel data of the image
        pixels = image.load()

        # Iterate through the binary content for the current page
        index = start_index
        for y in range(0, 720, resolution):
            for x in range(0, 1280, resolution):
                if index < end_index:
                    # Use the first bit to determine the color
                    pixel_color = black if binary_content[index] == '0' else white
                    index += 1
                else:
                    # If the binary content ends, use a different color
                    pixel_color = other_color

                # Set the color for a block of pixels based on resolution
                for dy in range(resolution):
                    for dx in range(resolution):
                        pixels[x + dx, y + dy] = pixel_color

        # Save the resulting image with a sequential filename
        output_image_path = f'{output_folder}/page_{page_number + 1}.png'
        image.save(output_image_path)

def images_to_binary(input_folder, resolution=8):
    # Initialize an empty string to store concatenated binary content
    concatenated_binary = ""

    # Get the list of image files in the input folder
    image_files = [file for file in os.listdir(input_folder) if file.endswith(".png")]

    # Sort the image files to maintain order
    image_files.sort()

    # Iterate through each image file
    for image_file in image_files:
        # Create the full path to the image file
        image_path = os.path.join(input_folder, image_file)

        # Open the image and get pixel data
        with Image.open(image_path) as img:
            pixels = img.load()

            # Iterate through each block of pixels in the image
            for block_y in range(0, img.height, resolution):
                for block_x in range(0, img.width, resolution):
                    # Extract the first bit (0 or 1) from the pixel color of the top-left pixel in the block
                    pixel_color = pixels[block_x, block_y]

                    # Skip grey pixels and consider only black and white
                    if pixel_color == (0, 0, 0) or pixel_color == (255, 255, 255):
                        bit_value = '1' if pixel_color == (255, 255, 255) else '0'
                        concatenated_binary += bit_value

    return concatenated_binary


def binary_to_zip_file(binary_string, output_zip_file):
    # Convert binary string to bytes
    binary_bytes = bytearray(int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8))

    # Write binary content to a zip file
    with open(output_zip_file, 'wb') as zip_file:
        zip_file.write(binary_bytes)