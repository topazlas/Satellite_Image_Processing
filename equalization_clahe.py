import os
import cv2
import numpy as np

def apply_clahe(input_path, output_path):
    # 입력 경로에서 모든 이미지 파일 가져오기
    image_files = [f for f in os.listdir(input_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]

    # CLAHE 생성
    clahe = cv2.createCLAHE(clipLimit=0.6, tileGridSize=(8, 8))

    # 입력 경로에서 출력 경로로 이미지를 읽어 CLAHE를 적용하고 저장
    for image_file in image_files:
        # 이미지 읽기
        img_path = os.path.join(input_path, image_file)
        img = cv2.imread(img_path)

        # BGR에서 YUV로 변경
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

        # 밝기 채널에 대해서 CLAHE 적용
        img_yuv[:,:,0] = clahe.apply(img_yuv[:,:,0])

        # YUV에서 BGR로 변경
        img_clahe = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

        # 결과 이미지 저장
        output_file = os.path.join(output_path, f"clahe_{image_file}")
        cv2.imwrite(output_file, img_clahe)

        # 원본과 결과 이미지 시각화
        cv2.imshow('Before', img)
        cv2.imshow('After', img_clahe)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # 입력 이미지가 있는 경로와 결과를 저장할 경로 지정
    input_directory = 'out_inc_sat/'
    output_directory = 'out_equalization_clahe/'

    # 결과를 저장할 디렉토리가 없으면 생성
    os.makedirs(output_directory, exist_ok=True)

    # 이미지에 CLAHE 적용
    apply_clahe(input_directory, output_directory)
