# Set Function.py

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
print(s1 & s2)
print(s1.intersection(s2))
print(s2.intersection(s1))

print('_' * 50)

# 합집합
print(s1 | s2)
print(s1.union(s2))
print(s2.union(s1))

print('_' * 50)

# 차집합
print(s1 - s2)
print(s1.difference(s2))

print(s2 - s1)
print(s2.difference(s1))

print('_' * 50)

# add: 값 1개만 추가
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# update: 값 여러개 추가
s1.update([4, 5, 6])
print(s1)

# remove: 특정 값 제거
s1.remove(2)
print(s1)

