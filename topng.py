import numpy as np
import cv2
def crack(integer):
	start = int(np.sqrt(integer))
	factor = integer / start
	while not is_integer(factor):
		start += 1
		factor = integer / start
	return int(factor), start
def is_integer(number):
	if int(number) == number:
		return True
	else:
		return False
def topng(s):
	if len(s) % 3 != 0:
		print(len(s), "无法被3整除")
		return False
	else:
		size = crack(int(len(s) / 3))
		img = np.zeros([size[0],size[1],3],np.uint8)
		cnt = 0
		for x in range(size[0]):
			for y in range(size[1]):
				for z in range(3):
					img[x,y,z] = int(s[cnt])
					cnt += 1
		cv2.imwrite('result.png', img)
		return True
fin = open(input("输入路径："), "rb")
s = fin.read()
fin.close()
if topng(s):
	print("转换成功")