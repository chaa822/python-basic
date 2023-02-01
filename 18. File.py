# file.py

# create & write
f = open("/Users/jeongjaeo/Documents/python/pythonProject/새파일.txt", "w")
for i in range(1, 11): # 1 ~ 10
	data = "%d번째 줄입니다.\n" % i
	f.write(data)
f.close()


# readline
f = open("/Users/jeongjaeo/Documents/python/pythonProject/새파일.txt", "r")
while True:
	line = f.readline()
	if not line: break
	print(line)
f.close()


# readlines
f = open("/Users/jeongjaeo/Documents/python/pythonProject/새파일.txt", "r")
lines = f.readlines()
for line in lines:
	print(line)
f.close()


# add data
f = open("/Users/jeongjaeo/Documents/python/pythonProject/새파일.txt", "a")
for num in range(11, 20):
	data = "%d번째 줄입니다.\n" % num
	f.write(data)
f.close()


# read
f = open("/Users/jeongjaeo/Documents/python/pythonProject/새파일.txt", "r")
data = f.read()
print(data)
f.close()


# with
with open("/Users/jeongjaeo/Documents/python/pythonProject/새파일.txt", "w") as f:
	f.write("Life is too short, you need python")

f = open("/Users/jeongjaeo/Documents/python/pythonProject/새파일.txt", "r")
data = f.read()
print(data)
f.close()