from utils.zip import *
from utils.images import *
from utils.video import *
from utils.encryption import *

file_path = "data/5mb.csv"
password = "test"

# Binary String
binary_string = convert_file_to_binary(file_path, password)

# # Make Image with Binary
# binary_to_images(binary_string, "data/initial_images/")

# # Make Video with Binary Images
# images_to_video("data/initial_images/", "videos/output_video.avi")

# # Extract Image back from Video
# video_to_images("videos/output_video.avi", "data/extracted_images")

# # Extract Binary from Concatenated Image 
# binary_res = images_to_binary("data/extracted_images/")

# # Make Zip file with binary
# binary_to_zip_file(binary_res, "data/zipped_files/5mb_back.zip")

# # Extract Original File
# unzip("data/zipped_files/5mb_back.zip", "extracted_files")