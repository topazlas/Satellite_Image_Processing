import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def scale_pixel_values(image, low_thresholds, high_thresholds):
    # Scale pixel values to the range [0, 255] for each channel
    for i in range(3):  # Iterate over RGB channels
        image[:, :, i] = np.clip(image[:, :, i], low_thresholds[i], high_thresholds[i])
        image[:, :, i] = np.interp(image[:, :, i], (low_thresholds[i], high_thresholds[i]), (0, 255))

    return image.astype(np.uint8)

def display_histogram(ax, image, title):
    # Calculate histogram for each RGB channel
    for i in range(3):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])
        ax.plot(histogram, label=f'Channel {i}')

    ax.set_title(title)
    ax.set_xlabel('Pixel Value')
    ax.set_ylabel('Frequency')
    ax.legend()

def main():
    # Load an image
    image_path = "out_inc_sat/increased_saturation_blended_image_alpha_0.4.jpg"
    original_image = cv2.imread(image_path)

    if original_image is None:
        print("Error: Image not loaded.")
        return

    # Create subplots in a single figure
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # Display the original image
    axes[0, 0].imshow(original_image[:, :, ::-1])  # OpenCV reads images in BGR, so convert to RGB for display
    axes[0, 0].set_title('Original Image')

    # Display the histogram of the original image
    display_histogram(axes[0, 1], original_image, 'Histogram - Original Image')

    # Set your desired pixel value ranges (adjust as needed)
    low_thresholds = [0, 0, 0]  # Example values, adjust as needed
    high_thresholds = [190, 190, 190]  # Example values, adjust as needed

    # Apply the histogram range and scale pixel values to [0, 255] for the image
    adjusted_image = scale_pixel_values(original_image.copy(), low_thresholds, high_thresholds)

    # Display the adjusted image
    axes[1, 0].imshow(adjusted_image[:, :, ::-1])  # OpenCV reads images in BGR, so convert to RGB for display
    axes[1, 0].set_title('Adjusted Image')

    # Display the histogram of the adjusted image
    display_histogram(axes[1, 1], adjusted_image, 'Histogram - Adjusted Image')

    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()

    # Save the adjusted image
    output_folder_path = "out_set_rgb_histogram_range/"
    os.makedirs(output_folder_path, exist_ok=True)
    output_image_path = os.path.join(output_folder_path, "scaled_" + os.path.basename(image_path))
    cv2.imwrite(output_image_path, adjusted_image)
    print(f"Processed image saved to: {output_image_path}")

if __name__ == "__main__":
    main()
