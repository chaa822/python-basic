# Try Catch.py
try:
	4 / 0
except ZeroDivisionError as e:
	print(e)

try:
	f = open("/Users/jeongjaeo/Documents/python/pythonProject/새파일.txt", "r")
except FileNotFoundError as e:
	print(str(e))
else:
	data = f.read()
	print(data)
	f.close()

f = open("/Users/jeongjaeo/Documents/python/pythonProject/새파일.txt", "r")
try:
	print(f.read())
except FileNotFoundError as e:
	print(str(e))
finally:
	f.close()


# 강제로 오류 발생 시키기
class Bird:
	def fly(self):
		raise NotImplementedError

# fly 메서드를 구현하지 않으면 에러
class Eagle(Bird):
	def fly(self):
		print("fly")

eagle = Eagle()
eagle.fly()