import cv2
import os
import matplotlib.pyplot as plt

def plot_image_and_histogram(ax, image, title):
    # 이미지 표시
    ax[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # BGR to RGB for proper display
    ax[0].set_title(title)

    # 히스토그램 계산
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

    # 히스토그램 표시
    ax[1].plot(histogram, color='black')
    ax[1].set_title('Histogram')
    ax[1].set_xlabel('Pixel Value')
    ax[1].set_ylabel('Frequency')

def normalize_image(image):
    # 이미지 정규화 (0~1 범위로)
    normalized_image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)
    return normalized_image

def process_images_in_folder(folder_path):
    # 폴더 내 모든 파일에 대해 반복
    for filename in os.listdir(folder_path):
        # 파일 경로 생성
        file_path = os.path.join(folder_path, filename)

        # 파일이 이미지인지 확인
        if os.path.isfile(file_path) and any(file_path.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg']):
            # 이미지 읽기
            color_image = cv2.imread(file_path)

            # 이미지 정규화
            normalized_image = normalize_image(color_image)

            # 새로운 figure 생성
            fig, ax = plt.subplots(2, 2, figsize=(12, 6))

            # 원본 이미지와 히스토그램 시각화
            plot_image_and_histogram(ax[0], color_image, f'Original Image and Histogram for {filename}')

            # 정규화된 이미지와 히스토그램 시각화
            plot_image_and_histogram(ax[1], normalized_image, f'Normalized Image and Histogram for {filename}')

            # plt에 표시
            plt.tight_layout()
            plt.show()

if __name__ == "__main__":
    folder_path = "Gray_Images/"  # 실제 폴더 경로로 대체해주세요
    process_images_in_folder(folder_path)
