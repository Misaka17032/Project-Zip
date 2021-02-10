fin = open("result", "r")
s = fin.read()
fin.close()
s = s.split(" ")
a = []
for i in s:
	try:
		a.append(int(i))
	except:
		pass
fout = open(input("输出文件："),"wb")
fout.write(bytes(a))
fout.close()