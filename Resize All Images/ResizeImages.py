import os
from PIL import Image


def resize_images(directory_path, target_path, target_height):
    # Get a list of all image files in the directory
    image_files = [file for file in os.listdir(
        directory_path) if file.endswith((".JPG", ".jpg", ".jpeg", ".png"))]

    # Iterate over each image file
    for file in image_files:
        try:
            # Get the path of the current image file
            image_path = os.path.join(directory_path, file)

            # Open the image file
            image = Image.open(image_path)

            # Calculate the new width based on the target height and the original aspect ratio
            aspect_ratio = image.width / image.height
            new_width = int(target_height * aspect_ratio)

            # Resize the image while maintaining the aspect ratio
            resized_image = image.resize((new_width, target_height))

            # Save the resized image with a new filename
            resized_image_path = os.path.join(
                target_path, f"{file}")
            resized_image.save(resized_image_path)

        except:
            print("Can't resize:", file)


# Example usage: Resize all images in the "images" directory to a height of 1000 pixels
resize_images("memes/OriginalMemes", "memes", 750)
