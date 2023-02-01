# String Function.py
a = "hobby"

# count: 변수 a안에 문자 "b"의 개수를 센다
print(a.count('b'))

a = "Python is best choice"

# find: 변수 a에서 문자 "b"가 처음으로 나온 위치(index)
print(a.find('b'))

# 없을 경우 -1 반환
print(a.find('k'))

# index: find와 같으나, 찾는 문자가 없으면 오류 발생
print(a.index('b'))

# error
# print(a.index('k'))

# 자바스크립트의 Arrays.join과 비슷한 기능
# 뒤의 문자열 사이사이에 앞의 문자열을 삽입
print(",".join("abcd"))

# UpperCase
a = "hi"
print(a.upper())

# lowerCase
a = "HI"
print(a.lower())

# 왼쪽 공백 삭제 := ltrim
a = " hi "
print(a.lstrip())

# 오른쪽 공백 삭제 := rtrim
print(a.rstrip())

# 양쪽 공백 삭제 := trim
print(a.strip())

# 문자열 바꾸기
a = "Life is too short"
print(a.replace("Life", "Your leg"))

# 문자열 나누기 := 기본 값이 space (공백)
print(a.split())

a = "a:b:c:d"
print(a.split(":"))

