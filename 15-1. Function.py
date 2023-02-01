# Function.py
def sum(a, b):
	return a + b

a = 3
b = 4
c = sum(a, b)
print(c)

# 입력 값이 없는 함수
def say():
	return 'Hi'

s = say()
print(s)

def sum(a, b):
	print("%d, %d의 합은 %d입니다." % (a, b, a + b))

sum(3, 4)
a = sum(3, 4)
print(a)

def sum_many(*args):
	sum = 0
	for num in args:
		sum = sum + num
	return sum

result = sum_many(1, 2, 3)
print(result)

result = sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

def sum_mul(choice, *args):
	if choice == 'sum':
		result = 0
		for num in args:
			result = result + num

	elif choice == 'mul':
		result = 1
		for num in args:
			result = result * num

	return result

result = sum_mul('sum', 1, 2, 3, 4, 5)
print(result)

result = sum_mul('mul', 1, 2, 3, 4, 5)
print(result)

# return tuple
def sum_and_mul(a, b):
	return a + b, a * b

result = sum_and_mul(3, 4)
print(result)

sum, mul = sum_and_mul(3, 4)
print(sum)
print(mul)

def say_nick(nick):
	if nick == "바보":
		return
	print("나의 별명은 %s입니다." % nick)

say_nick("야호")
say_nick("바보")

# parameter default setting
def say_myself(name, old, man=True):
	print("나의 이름은 %s 입니다." % name)
	print("나이는 %d살 입니다." % old)
	if man:
		print("남자입니다.")
	else:
		print("여자입니다.")

say_myself("재오", 34)
say_myself("재오", 34, True)
say_myself("재순", 24, False)

