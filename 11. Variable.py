# Variable.py
import sys

a = 1
b = 'python'
c = [1, 2, 3]

print(type(a))
print(type(b))
print(type(c))

a = 3
print(sys.getrefcount(3))

b = 3
print(a is b)
print(sys.getrefcount(3))

c = 3
print(sys.getrefcount(3))


a, b = ('python', 'life')
print(a)
print(b)

(a, b) = 'python', 'life'
print(a)
print(b)

[a, b] = ['python', 'life']
print(a)
print(b)

a = b = 'python'
print(a)
print(b)

a = 3
b = 5
a, b = b, a
print(a)
print(b)

a = [1, 2, 3]
b = a
a[1] = 4
print(a)
print(b)

# 리스트 복사
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

from copy import copy
c = copy(a)
print(a is c)
