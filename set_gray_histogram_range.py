import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

def scale_pixel_values(image, low_threshold, high_threshold):
    # Scale pixel values to the range [0, 255] for the single channel
    image = np.clip(image, low_threshold, high_threshold)
    image = np.interp(image, (low_threshold, high_threshold), (0, 255))

    return image.astype(np.uint8)

def display_histogram(ax, image, title):
    # Calculate histogram for the single channel
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    ax.plot(histogram, label='Channel 0')

    ax.set_title(title)
    ax.set_xlabel('Pixel Value')
    ax.set_ylabel('Frequency')
    ax.legend()


def main():
    # Load a grayscale image
    image_path = "1.jpg"
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if original_image is None:
        print("Error: Image not loaded.")
        return

    # Create subplots in a single figure
    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

    # Display the original image
    axes[0, 0].imshow(original_image, cmap='gray')
    axes[0, 0].set_title('Original Image')

    # Display the histogram of the original image
    display_histogram(axes[0, 1], original_image, 'Histogram - Original Image')

    # Set your desired pixel value ranges (adjust as needed)
    low_threshold = 20  # Example value, adjust as needed
    high_threshold = 120  # Example value, adjust as needed

    # Apply the histogram range and scale pixel values to [0, 255] for the image
    adjusted_image = scale_pixel_values(original_image.copy(), low_threshold, high_threshold)

    # Display the adjusted image
    axes[1, 0].imshow(adjusted_image, cmap='gray')
    axes[1, 0].set_title('Adjusted Image')

    # Display the histogram of the adjusted image
    display_histogram(axes[1, 1], adjusted_image, 'Histogram - Adjusted Image')

    # Adjust layout and show the plot
    plt.tight_layout()
    plt.show()

    # Save the adjusted image with threshold values in the filename
    output_folder_path = "out_set_gray_histogram_range/"
    os.makedirs(output_folder_path, exist_ok=True)

    # Construct the output image filename with threshold values
    output_image_filename = f"scaled_threshold_{low_threshold}_{high_threshold}_{os.path.basename(image_path)}"
    output_image_path = os.path.join(output_folder_path, output_image_filename)

    cv2.imwrite(output_image_path, adjusted_image)
    print(f"Processed image saved to: {output_image_path}")


if __name__ == "__main__":
    main()

