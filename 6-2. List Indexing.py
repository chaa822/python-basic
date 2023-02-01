# List Indexing.py

list = [1, 2, 3]
print(list)

# 인덱스 양수: 오른쪽으로 이동
print(list[0] + list[1])

# 인덱스 음수: 왼쪽으로 이동
print(list[-1])

# 이중 리스트
list = [1, 2, 3, ['a', 'b', 'c']]
print(list[0])
print(list[-1])
print(list[3])

# list의 list 접근
print(list[-1][0])
print(list[-1][1])
print(list[-1][2])

# 삼중 리스트
list = [1, 2, ['a', 'b', ['Life', 'is']]]
print(list[2][2][0])