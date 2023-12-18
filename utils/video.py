import cv2
import os
import ffmpeg
import numpy as np

def images_to_video(input_folder, output_video_path, fps=30):
    # Get the list of image files in the input folder
    image_files = [file for file in os.listdir(input_folder) if file.endswith(".png")]

    # Sort the image files to maintain order
    image_files.sort(key=lambda x: int(x.split("_")[1].split(".")[0]))

    # Get the dimensions of the first image
    first_image_path = os.path.join(input_folder, image_files[0])
    first_image = cv2.imread(first_image_path)
    height, width, _ = first_image.shape

    # Create a VideoWriter object
    fourcc = 0  # Uncompressed Video
    video_writer = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Iterate through each image file and write frames to the video
    for image_file in image_files:
        print(image_file)
        image_path = os.path.join(input_folder, image_file)
        frame = cv2.imread(image_path)
        video_writer.write(frame)

    # Release the VideoWriter object
    video_writer.release()

def video_to_images(input_video_path, output_folder):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(input_video_path)

    # Get video properties
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Read and save each frame
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Save the frame as an image
        image_path = os.path.join(output_folder, f'page_{frame_count + 1}.png')
        cv2.imwrite(image_path, frame)

        frame_count += 1

    # Release the video capture object
    cap.release()

    print(f"Extracted {frame_count} frames from the video.")