from utils.zip import *
from utils.images import *
from utils.video import *
from utils.encryption import *
from utils.youtube import upload_video
from dotenv import load_dotenv
from utils.common import empty_folder, add_to_db, generate_md5
import os

file_name = "5mb.csv"
folder = "short_files"
password = "<password>"
# binary_string = convert_file_to_binary(file_name, password)
# #TODO: Clean initial_images folder
# empty_folder("data/initial_images/")
# # Convert to Images
# binary_to_images(binary_string, "data/initial_images/")
# # # Make Video with Binary Images
# images_to_video("data/initial_images/", "data/videos/output_video.avi")

yt_video_name = generate_md5(file_name)
video_id = upload_video("data/videos/output_video.avi", yt_video_name)
add_to_db(folder, file_name, yt_video_name, video_id, password)

# Extract Image back from Video
# TODO: Clean extracted_images folder first
# video_to_images("data/videos/output_video.avi", "data/extracted_images")

# # Extract Binary from Concatenated Image 
# binary_res = images_to_binary("data/extracted_images/")

# # Make Zip file with binary
# binary_to_zip_file(binary_res, "data/zipped_files/5mb_back.zip")

# # Extract Original File
# unzip("data/zipped_files/5mb_back.zip", "data/extracted_files")
