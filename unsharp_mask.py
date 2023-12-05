import os
import cv2

def apply_unsharp_masking(image_path, output_path):
    # Read the image
    image = cv2.imread(image_path)

    # Apply unsharp masking
    gaussian_3 = cv2.GaussianBlur(image, (9, 9), 10.0)
    sharpened_image = cv2.addWeighted(image, 8, gaussian_3, -7, 0, image)

    # Save the result
    output_filename = os.path.join(output_path, os.path.basename(image_path))
    cv2.imwrite(output_filename, sharpened_image)
    print(f"Processed: {output_filename}")

def apply_unsharp_masking_to_all_images(input_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Process each image
    for image_file in image_files:
        input_path = os.path.join(input_folder, image_file)
        apply_unsharp_masking(input_path, output_folder)

if __name__ == "__main__":
    # User-defined input and output paths
    input_folder_path = "out_inc_sat/"
    output_folder_path = "out_unsharp_mask/"

    # Apply unsharp masking to all images in the input folder and save results to the output folder
    apply_unsharp_masking_to_all_images(input_folder_path, output_folder_path)
