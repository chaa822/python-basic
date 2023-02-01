# String Slice
# 0 <= 인덱스 < N

a = "Life is too short, You need Python"

print(a[0:4]) # Life

print(a[0:2]) # Li

print(a[5:7]) # is

print(a[12:17]) # short

print(a[19:]) # index 19 ~ end

print(a[:17]) # index 0 ~ 16

print(a[:]) # 전체

print(a[19:-7]) # index 19에서 뒤로 7

# 슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date = a[:8]	# index 0 ~ 7 := 20010331
weather = a[8:]	# index 8 ~ end := Rainy
print(date)
print(weather)

year = a[:4]	# 2001
month = a[4:6]	# 03
day = a[6:8]	# 31
weather = a[8:]	# Rainy

print(year)
print(month)
print(day)
print(weather)

# Pithon -> Python으로 바꾸기
a = "Pithon"
print(a[:1] + "y" + a[2:])