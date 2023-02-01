# for.py
test_list = ['one', 'two', 'three']
for i in test_list:
	print(i)

a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
	print(first + last)

# marks1.py
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
	number = number + 1
	if mark >= 60:
		print("%d 번 학생은 합격입니다." % number)
	else:
		print("%d 번 학생은 불합격입니다." % number)

# marks2.py
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
	number = number + 1
	if mark < 60: continue
	print("%d번 학생 축하합니다. 합격입니다." % number)

# range.py

# range(10): 0 ~ 9까지의 숫자
for v in range(10):
	print(v)

sum = 0
# range(1, 11): 1 ~ 10까지의 숫자
for v in range(1, 11):
	sum = sum + v

print(sum)


# marks3.py
marks = [90, 25, 67, 45, 80]

# len(marks): marks의 개수 (size)
print(len(marks))

# range(len(marks)): 0 ~ 4 (marks의 길이 - 1)
for number in range(len(marks)):
	if marks[number] < 60: continue
	print("%d번 학생 축하합니다. 합격입니다." % (number + 1))


# gugudan.py

for i in range(2, 10):
	for j in range(1, 10):
		print(i * j, end=" ")
	print('')

# for in list.py

result = []
a = [1, 2, 3, 4]

for num in a:
	result.append(num * 3)

print(result)

result = [num * 3 for num in a]
print(result)

result = [x * y for x in range(2, 10)
		  for y in range(1, 10)]
print(result)