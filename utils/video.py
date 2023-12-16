import cv2
import os
import ffmpeg
import numpy as np

def images_to_video(input_folder, output_folder, output_video):
    # Get a list of all image files in the folder
    image_files = [f for f in os.listdir(input_folder) if f.endswith('.png')]

    # Sort the files based on their names (assuming they are named sequentially)
    image_files.sort(key=lambda x: int(x.split('.')[0]))

    # Get the dimensions of the first image
    first_image = cv2.imread(os.path.join(input_folder, image_files[0]))
    height, width, layers = first_image.shape

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Create a VideoWriter object with a fixed frame rate of 24 fps
    video_path = os.path.join(output_folder, output_video)
    video = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*'raw '), 24, (width, height))


    # Iterate through each image file and write to the video
    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        img = cv2.imread(image_path)
        video.write(img)

    # Release the VideoWriter
    video.release()


def video_to_images(input_video, output_folder):
    # Extract frame unit16 arrays from the video
    ffmpeg_executable = r"C:\\ffmpeg\\bin\\ffmpeg.exe"
    # Extract frame unit16 arrays from the video
    def extract_frame(input_vid, frame_num):
        try:
            out, _ = (
                ffmpeg
                .input(input_vid, executable=ffmpeg_executable)
                .filter_('select', 'gte(n,{})'.format(frame_num))
                .output('pipe:', format='rawvideo', pix_fmt='gray16le', vframes=1)
                .run(capture_stdout=True, capture_stderr=True)
            )
            return np.frombuffer(out, np.uint16).reshape([720, 1280])
        except ffmpeg._run.Error as e:
            print(f"ffmpeg error: {e.stderr.decode('utf-8')}")

    # Get the total number of frames in the video
    total_frames = 3  # Replace with the actual total number of frames

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through each frame and save it as an image
    for i in range(total_frames):
        frame = extract_frame(input_video, i)
        frame_name = f"{i + 1}.png"
        frame_path = os.path.join(output_folder, frame_name)
        cv2.imwrite(frame_path, frame)