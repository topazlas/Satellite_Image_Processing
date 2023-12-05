import cv2
import os
import matplotlib.pyplot as plt

def plot_image_and_rgb_histogram(image, title):
    # 새로운 figure 생성
    plt.figure(figsize=(18, 6))

    # 이미지 표시
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)

    # R, G, B 각각의 색상에 대한 히스토그램 계산 및 표시
    colors = ('r', 'g', 'b')
    for i, color in enumerate(colors):
        histogram = cv2.calcHist([image], [i], None, [256], [0, 256])

        # 히스토그램 표시
        plt.subplot(1, 2, 2)
        plt.plot(histogram, color=color, label=f'{color.upper()}')
        plt.title('RGB Histogram')
        plt.xlabel('Pixel Value')
        plt.ylabel('Frequency')

    # 범례 추가
    plt.legend()

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
            # 컬러 이미지 읽기
            color_image = cv2.imread(file_path)

            # 이미지와 RGB 히스토그램 시각화
            plot_image_and_rgb_histogram(color_image, f'Image and RGB Histogram for {filename}')

if __name__ == "__main__":
    folder_path = "Color_Processed_Images/"  # 실제 폴더 경로로 대체해주세요
    process_images_in_folder(folder_path)
