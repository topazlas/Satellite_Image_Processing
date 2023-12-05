import cv2
import numpy as np

def onChange(alpha, img1, img2):
    # Ensure img1 and img2 have the same size and number of channels
    if img1.shape != img2.shape:
        print("Error: Input images must have the same size and number of channels.")
        return

    # Perform image blending
    dst = cv2.addWeighted(img1, 1 - alpha, img2, alpha, 0)

    # Display the blended image
    cv2.imshow(win_name, dst)

    # Update global variables for alpha and blended image
    global current_alpha, blended_image
    current_alpha = alpha
    blended_image = dst

# Load your images (img1 and img2) here
img1 = cv2.imread("out_set_gray_histogram_range/scaled_threshold_20_120_1.jpg")
img2 = cv2.imread("2.jpg")

# Check if the images are loaded successfully
if img1 is None or img2 is None:
    print("Error: One or both images could not be loaded.")
else:
    # Create a window
    win_name = 'Blended Image'
    cv2.namedWindow(win_name)

    # Create a trackbar
    trackbar_name = 'Alpha'
    cv2.createTrackbar(trackbar_name, win_name, 0, 100, lambda x: onChange(x / 100.0, img1, img2))

    # Display the initial images
    onChange(0, img1, img2)

    # Wait for a key event
    while True:
        k = cv2.waitKey(1) & 0xFF

        # Save the image when the 's' key is pressed
        if k == ord('s'):
            save_path = "out_alpha_blending/blended_image_alpha_{}.jpg".format(current_alpha)
            cv2.imwrite(save_path, blended_image)
            print(f"Blended image saved to: {save_path}")

        # Close the window on 'Esc'
        elif k == 27:
            break

    cv2.destroyAllWindows()
