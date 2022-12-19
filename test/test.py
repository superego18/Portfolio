from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

icon = Image.open('image-removebg-preview.png') # 이미지 파일 읽어오기
mask = Image.new("RGB", icon.size, (255,255,255))
mask.paste(icon,icon)
mask_img = np.array(mask) # 픽셀 값 배열 형태 변환

# def transform_zeros(val):
#     if val == 0:
#         return 255
#     else:
#         return val

# maskable_image = np.ndarray((mask_img.shape[0],mask_img.shape[1]), np.int32)

# for i in range(len(mask_img)):
#     maskable_image[i] = list(map(transform_zeros, mask_img[i]))

print(mask_img)

np.savetxt('test.txt', mask_img, fmt = '%3d', delimiter = ',', header='test')  