# built-in function

# abs
print(abs(3))
print(abs(-3))
print(abs(-1.2))

# all
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))

# any
print(any([1, 2, 3, 0]))
print(any([0, ""]))

# chr
print(chr(97))
print(chr(48))

# divmod
print(divmod(7, 3))
print(divmod(1.3, 0.2))

# enumerate
for index, value in enumerate(['body', 'foo', 'bar']):
	print(index, value)

# eval
print(eval('1+2'))
print(eval("'hi' + 'a'"))

# filter
def positive(l):
	result = []
	for i in l:
		if i > 0:
			result.append(i)
	return result
print(positive([1, -3, 2, 0, -5, 6]))

def positive(x):
	return x > 0
print(list(filter(positive, [1, -3, 2, 0, -5 ,6])))

# hex
print(hex(234))
print(hex(3))

# id
a = 3
print(id(3))
print(id(a))
b = a
print(id(b))

# int
print(int('3'))
print(int(3.4))

# isinstance
class Person:
	pass
a = Person()
print(isinstance(a, Person))
b = 3
print(isinstance(b, Person))

# lambda
sum = lambda a, b : a + b
print(sum(3, 4))

myList = [lambda a, b : a + b, lambda a, b : a * b]
print(myList[0](3, 4))
print(myList[1](3, 4))

# len
print(len("python"))
print(len([1, 2, 3]))
print(len((1, 'a')))

# list
print(list("python"))
print(list((1, 2, 3)))

# 리스트 복사
a = [1, 2, 3]
b = list(a)
print(b)

# map
def two_times(numberList):
	result = []
	for number in numberList:
		result.append(number * 2)
	return result

result = two_times([1, 2, 3, 4])
print(result)

def two_times(x):
	return x * 2

print(list(map(two_times, [1, 2, 3, 4])))
print(list(map(lambda x : x * 2, [1, 2, 3, 4])))

# max
print(max([1, 2, 3]))
print(max("python"))

# min
print(min([1, 2, 3]))
print(min("python"))

# pow
print(pow(2, 4))
print(pow(3, 3))

# range
print(list(range(5)))
print(list(range(5, 10)))
print(list(range(1, 10, 2)))
print(list(range(0, -10, -1)))

print(sorted([3, 1, 2]))
print(sorted(['b', 'a', 'c']))
print(sorted('zero'))
print(sorted((3, 2, 1)))

# str
print(str(3))

# tuple
print(tuple("abc"))
print(tuple([1, 2 ,3]))

print(type("abc"))
print(type([]))
print(type(open("test", "w")))