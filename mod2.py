# mod2.py
PI = 3.14592

class Math:
	def solv(slef, r):
		return PI * (r * 2)

def sum(a, b):
	return a + b

if __name__ == "__main__":
	print(PI)
	a = Math()
	print(a.solv(2))
	print(sum(PI, 4.4))