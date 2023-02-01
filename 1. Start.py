# Start.py

print("______________________")

# 복소수의 연산도 가능
a = 2 + 3j
b = 3
print(a * b)

print("______________________")

a = 3
# 변수 a가 1보다 크면 출력한다
if a > 1:
    print("a is greater than 1")

print("______________________")

# 변수 a에 1, 2, 3을 대입하여 출력한다 := for(int i = 1; i <= 3; i += 1)
for a in [1, 2, 3]:
    print(a)

print("______________________")

# while
i = 0
while i < 3:
    i = i + 1
    print(i)

print("______________________")

def sum(a, b):
    return a + b

sum = sum(1, 2)
print(sum)

"""
여러줄의 주석을 작성합니다
여러줄의 주석을 작성합니다
여러줄의 주석을 작성합니다
"""