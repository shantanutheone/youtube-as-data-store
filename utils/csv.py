import pandas as pd
from PIL import Image
import base64
import numpy as np
import math
import os

# def csv_to_image(csv_file, image_file):
#     df = pd.read_csv(csv_file)

#     csv_content = df.to_csv(index=False)

#     binary_data = base64.b64encode(csv_content.encode('utf-8'))

#     pixels = [int(bit) for bit in binary_data]

#     image_array = np.array(pixels, dtype=np.uint8)

#     image_array = np.reshape(image_array, (1, len(pixels)))
#     image = Image.fromarray(image_array, 'L')

#     image.save(image_file)

def csv_to_images(csv_file, output_folder):
    # Read CSV file
    df = pd.read_csv(csv_file)

    # Convert DataFrame to CSV string
    csv_content = df.to_csv(index=False)

    # Convert CSV string to binary
    binary_data = base64.b64encode(csv_content.encode('utf-8'))

    # Convert binary to list of integers without scaling
    pixels = [int(bit) for bit in binary_data]

    # Determine the target image size (1920x1080 pixels)
    target_size = (1080, 1920)

    # Calculate the total number of pixels in the data
    total_pixels = len(pixels)

    # Calculate the number of images needed
    num_images = math.ceil(total_pixels / (target_size[0] * target_size[1]))

    # Split the pixels into chunks for each image
    pixel_chunks = [pixels[i * (target_size[0] * target_size[1]): (i + 1) * (target_size[0] * target_size[1])] for i in range(num_images)]

    # Create and save images
    for i, pixel_chunk in enumerate(pixel_chunks):
        # Resize the image array to match the target size
        image_array = np.resize(pixel_chunk, target_size)

        # Create an image from the array
        image = Image.fromarray(image_array, 'L')

        # Save the image with sequential names
        image_file = f"{output_folder}/{i + 1}.png"
        image.save(image_file)


# def image_to_csv(image_file, csv_file):
#     image = Image.open(image_file)

#     image_array = np.array(image)

#     flattened_array = image_array.flatten()

#     binary_data_back = bytes(flattened_array)

#     csv_content = base64.b64decode(binary_data_back.decode('utf-8'))
    
#     with open(csv_file, 'wb') as file:
#         file.write(csv_content)
        

def images_to_csv(input_folder, csv_file):
    # Get a list of all image files in the folder
    image_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]

    # Initialize an empty list to store pixel data from all images
    all_pixels = []

    # Iterate through each image file
    for image_file in image_files:
        # Open the image
        image = Image.open(os.path.join(input_folder, image_file))

        # Convert the image to a numpy array
        image_array = np.array(image)

        # Flatten the array to 1D
        flattened_array = image_array.flatten()

        # Extend the list with the pixel data from the current image
        all_pixels.extend(flattened_array)

    # Convert the list of integers to bytes
    combined_binary_data = bytes(all_pixels)

    # Decode binary data to CSV content
    csv_content = base64.b64decode(combined_binary_data.decode('utf-8'))

    # Save the CSV content to a file
    with open(csv_file, 'wb') as file:
        file.write(csv_content)


