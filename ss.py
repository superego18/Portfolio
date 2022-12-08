from PIL import Image
import numpy as np
im = Image.open('./son.png') # 이미지 파일 읽어오기
mask_arr = np.array(im) # 픽셀 값 배열 형태 변환

print(mask_arr)