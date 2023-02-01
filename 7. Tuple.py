# Tuple.py

t1 = ()
t2 = (1,) # 하나만 할당할 경우 콤마 필수
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

# 인덱싱하기
t1 = (1, 2, 'a', 'b')
print(t1[0])
print(t1[3])

# 슬라이싱하기
t1 = (1, 2, 'a', 'b')
print(t1[1:])

# 더하기
t2 = (3, 4)
print(t1 + t2)

# 곱하기
print(t2 * 3)