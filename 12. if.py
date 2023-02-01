# if.py

money = 1
if money:
	print('택시를 타고 가라')
else:
	print('걸어 가라')


x = 3
y = 2
print(x > y)
print(x < y)
print(x == y)
print(x != y)

money = 3000
if money >= 3000:
	print('택시를 타고 가라')
else:
	print('걸어 가라')

money = 2000
card = 1
if money >= 3000 or card:
	print('택시를 타고 가라')
else:
	print('걸어 가라')

print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

print('a' in ('a', 'b', 'c'))
print('j' not in 'python')


pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
	print('택시를 타고 가라')
else:
	print('걸어 가라')


if 'money' in pocket:
	pass
else:
	print('걸어 가라')


if 'money' in pocket:
	print('택시를 타고 가라')
elif card:
	print('택시를 타고 가라')
else:
	print('걸어 가라')

