def tozip(s):
	pass
fin = open(input("输入路径："), "rb")
s = fin.read()
fin.close()
s = tozip()
fout = open("result","w")
t = ""
for i in s:
	t += str(i) + " "
fout.write(t)
fout.close()