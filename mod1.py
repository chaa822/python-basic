# mod1.py

def sum(a, b):
	return a + b

def safe_sum(a, b):
	if type(a) != type(b):
		print("더할 수 있 것이 아닙니다.")
		return
	else:
		result = a + b

	return result

if __name__ == "__main__":
	print(safe_sum('a', 1))
	print(safe_sum(1, 4))
	print(safe_sum(10, 10.4))