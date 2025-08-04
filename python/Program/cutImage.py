// 이미지를 원하는 크기로 등분하는 프로그램.
from PIL import Image

# 원본 이미지 열기
source_image = Image.open(r"2D/Drop King/assets/Scene/background/originalBackground/background09.webp")


# 잘라낼 크기 (4:3 비율 = 310x232)
slice_width = 666
slice_height = 500

# 이미지 전체 높이에서 자를 수 있는 영역 계산
image_width, image_height = source_image.size
num_slices = image_height // slice_height

# 슬라이스 반복
for i in range(num_slices):
    top = i * slice_height
    box = (0, top, slice_width, top + slice_height)
    cropped = source_image.crop(box)
    cropped.save(f"background{i + 11}.png")

print(f"{num_slices}개 이미지로 잘라 저장 완료!")
