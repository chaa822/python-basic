# Function Scope4.py
# 비추천
a = 1

def vartest():
	global a
	a = a + 1

vartest()
print(a)