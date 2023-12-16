from utils.csv import csv_to_images, images_to_csv
from utils.video import images_to_video, video_to_images

csv_file_path = 'data/10mb.csv'

# Defaults
csv_to_images_folder = "csv_frames"
video_to_images_folder = "video_frames"
videos_folder = "videos"
video_name = "output_video.mp4"

# # Convert CSV to image
# csv_to_images(csv_file_path, csv_to_images_folder)

# # Convert image back to CSV
# # images_to_csv(images_folder, csv_file_path_back)

# # Example usage:
# images_to_video(csv_to_images_folder, videos_folder, video_name)

video_to_images('videos/output_video1.mp4', 'video_frames')
# csv_file_path_back = csv_file_path.split(".")[0] + "_back.csv"
# images_to_csv(video_to_images_folder, csv_file_path_back)