from PIL import Image
import os

def resize_and_convert_to_rgb(input_dir, output_dir, target_size=(256, 256)):
    """
    Resize images in input_dir to target_size and convert them to RGB format.
    
    Args:
    input_dir (str): Path to the directory containing input images.
    output_dir (str): Path to the directory where resized and converted images will be saved.
    target_size (tuple): Target size of the images in the format (width, height).
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate over each file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            # Open the image file
            with Image.open(os.path.join(input_dir, filename)) as img:
                # Convert the image to RGB format (if it's not already in RGB)
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Resize the image
                img_resized = img.resize(target_size, Image.ANTIALIAS)
                
                # Save the resized and converted image to the output directory
                img_resized.save(os.path.join(output_dir, filename))

# Example usage:
input_directory = "C:\\Users\\Paramanna Patil\\Desktop\\AI_Project\\pics\\3"
output_directory = "C:\\Users\\Paramanna Patil\\Desktop\\AI_Project\\Dataset\\train\\3"

resize_and_convert_to_rgb(input_directory, output_directory)