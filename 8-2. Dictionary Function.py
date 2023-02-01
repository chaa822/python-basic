# Dictionary Function.py

# keys: key 리스트 만들기
a = {'name': 'pey', 'phone': '0109993323', 'birth': '1118'}
print(a.keys())
print(list(a.keys()))

for k in a.keys():
	print(k)

# values: value 리스트 만들기
print(a.values())
print(list(a.values()))

for v in a.values():
	print(v)

# key, value로 구성된 item 리스트 가져오기
print(a.items())
print(list(a.items()))

for item in a.items():
	print(item)

# 초기화
a.clear()
print(a)

a = {'name': 'pey', 'phone': '0109993323', 'birth': '1118'}
print(a.get('name'))
print(a.get('phone'))
print(a.get('birth'))

# getDefault - 값이 없을 경우를 대비해 기본 값 지정
print(a.get('foo', 'bar'))

# in : key에 값이 있는지 확인 (boolean)
print('name' in a)

