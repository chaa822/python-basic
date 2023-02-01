# String Formatting.py

# 숫자 대입
a = "I eat %d apples." % 3
print(a)

# 문자열 대입
b = "I eat %s apples." % "five"
print(b)

# 변수 대입
number = 3
c = "I eat %d apples." % number
print(c)

# 2개 이상의 값 넣기
number = 10
day = "three"
d = "I ate %d apples. so I was sick for %s days." % (number, day)
print(d)

# 포맷팅에서 %를 사용하려면 %%
e = "Error is %d%%." % 98
print(e)

# 정렬과 공백
# 전체 길이가 10개인 문자열 공간에서 hi를 오른쪽으로 정렬하고 그 앞의 나머지는 공백
f = "%10s " % "hi"
print(f)

# 전체 길이가 10개인 문자열 공간에서 hi를 왼쪽으로 정렬하고 그 뒤의 나머지는 공백
f = "%-10sjane" % "hi"
print(f)

# 소수점 표현
# 0.4 := 소수점 4자리만
g = "%0.4f" % 3.42134234
print(g)