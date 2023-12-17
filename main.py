from utils.zip import *
from utils.images import *
from utils.video import *

file_path = "data/5mb.csv"

# Binary String
binary_string = convert_file_to_binary(file_path)

# Make Image with Binary
binary_to_images(binary_string, "data/initial_images/")

# Test by making back csv with images - Done
# binary_res = images_to_binary("data/initial_images")
# print(binary_res == binary_string)
# binary_to_zip_file(binary_res, "data/zipped_files/5mb_back.zip")
# unzip("data/zipped_files/5mb_back.zip", "extracted_files")

# Make Video with Binary Images
images_to_video("data/initial_images/", "videos/output_video.avi")

# Extract Image back from Video

# Extract Binary from Concatenated Image 

# Make Zip file with binary

# Extract Original File

