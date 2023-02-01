# List Slice.py

list = [1, 2, 3, 4, 5]

# [startIndex:endIndex-1]
print(list[0:2])

print('_' * 50)

a = [1, 2, 3]
b = a[:2]
c = a[2:]

print(a)
print(b)
print(c)

print('_' * 50)

# 중첩된 리스트 슬라이싱하기
list = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(list[2:5])
print(list[3][:2])