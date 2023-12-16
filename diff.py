from PIL import Image, ImageChops

def image_difference(image_path1, image_path2, output_path=None):
    # Open the images
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)

    # Ensure the images have the same size
    if image1.size != image2.size:
        raise ValueError("Images must have the same dimensions for comparison.")

    # Calculate the absolute difference between the two images
    diff = ImageChops.difference(image1, image2)

    # Convert the difference image to grayscale
    diff = diff.convert('L')

    # Save or show the difference image
    if output_path:
        diff.save(output_path)
    else:
        diff.show()

# Example usage:
image_difference('csv_frames/1.png', 'video_frames/1.png', 'difference.png')