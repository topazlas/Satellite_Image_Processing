import cv2
import os
import matplotlib.pyplot as plt

def plot_image_and_histogram(image, title):
    # 새로운 figure 생성
    plt.figure(figsize=(12, 6))

    # 이미지 표시
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # BGR to RGB for proper display
    plt.title(title)

    # 히스토그램 계산
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])

    # 히스토그램 표시
    plt.subplot(1, 2, 2)
    plt.plot(histogram, color='black')
    plt.title('Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    # 창 크기 조절
    plt.tight_layout()
    plt.show()

def process_images_in_folder(folder_path):
    # 폴더 내 모든 파일에 대해 반복
    for filename in os.listdir(folder_path):
        # 파일 경로 생성
        file_path = os.path.join(folder_path, filename)

        # 파일이 이미지인지 확인
        if os.path.isfile(file_path) and any(file_path.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg']):
            # 이미지 읽기
            color_image = cv2.imread(file_path)

            # 이미지와 히스토그램 시각화
            plot_image_and_histogram(color_image, f'Image and Histogram for {filename}')

if __name__ == "__main__":
    folder_path = "out_gray_nomalize/"  # 실제 폴더 경로로 대체해주세요
    process_images_in_folder(folder_path)
