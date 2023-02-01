# List Operation.py

# 더하기
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

# 곱하기
print(a * 3)

# 숫자와 문자를 더할 경우 오류가 발생할 수 있으므로
# str 함수를 사용해 숫자를 문자로 변경한 후 연산
print(str(a[2]) + 'hi')

print('_' * 50)

# 리스트 수정
a = [1, 2, 3]
a[2] = 4
print(a)

# 연속된 값 수정
print(a[1:2])

# 중간에 'a', 'b', 'c' 값을 삽입
a[1:2] = ['a', 'b', 'c']
print(a)

# 중간에 ['a', 'b', 'c'] 리스트를 삽입
# a[1] = ['a', 'b', 'c']
# print(a)

# [] 사용해 리스트 요소 삭제
a[1:3] = []
print(a)

# del 함수 사용
del a[1]
print(a)