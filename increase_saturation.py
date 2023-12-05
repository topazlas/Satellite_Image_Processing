import cv2
import os
import numpy as np

def increase_saturation(image_path, save_path, saturation_factor=5):
    # Read the image
    img = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if img is None:
        print(f"Error: Image not loaded from {image_path}")
        return

    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Increase the saturation
    hsv[:, :, 1] = hsv[:, :, 1] * saturation_factor

    # Clip the values to be in the valid range
    hsv[:, :, 1] = np.clip(hsv[:, :, 1], 0, 255)

    # Convert HSV back to BGR
    result_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # Save the processed image
    filename = os.path.basename(image_path)
    save_path = os.path.join(save_path, f"increased_saturation_{filename}")
    cv2.imwrite(save_path, result_img)
    print(f"Processed image saved to: {save_path}")

def process_images_in_folder(folder_path, save_path):
    # Create the save directory if it doesn't exist
    os.makedirs(save_path, exist_ok=True)

    # Process each image in the folder
    for filename in os.listdir(folder_path):
        # Check if the file is an image (you can add more image extensions as needed)
        if any(filename.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg']):
            # Generate the full file paths
            file_path = os.path.join(folder_path, filename)

            # Process and save the image
            increase_saturation(file_path, save_path)

if __name__ == "__main__":
    # Specify the input and output directories
    input_folder_path = "out_alpha_blending/"
    output_folder_path = "out_increase_saturation/"

    # Process images in the input folder and save them to the output folder
    process_images_in_folder(input_folder_path, output_folder_path)
