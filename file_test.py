f = open("test.txt", "w+")
num = f.write("我正在学习Python语言！\nPython语言简单又方便！")
print("写入的字符数：", num)
f = open("test.txt", 'r')
s = f.read()
print(s)
f = open("test.txt", "r")
s = f.readline()
print(s)

f.close()

