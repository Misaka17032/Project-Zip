import numpy as np
import cv2
img = cv2.imread("result.png")
a = []
for x in range(img.shape[0]):
	for y in range(img.shape[1]):
		for z in range(3):
			try:
				a.append(int(img[x][y][z]))
			except:
				pass
fout = open(input("输出文件："),"wb")
fout.write(bytes(a))
fout.close()