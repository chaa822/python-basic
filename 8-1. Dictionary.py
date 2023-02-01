# Dictionary.py

dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
a = {1: 'hi'}
b = {'a': [1, 2, 3]}

print(dic)
print(a)
print(b)

print('_' * 50)

# 추가
a = {1: 'a'}
a[2] = 'b'
print(a)
a['name'] = 'pey'
print(a)
a[3] = [1, 2, 3]
print(a)

# 값 가져오기
grade = {'pey': 10, 'juliet': 99}
print(grade['pey'])
print(grade['juliet'])

a = {1: 'a', 2: 'b'}
print(a[1])
print(a[2])

a = {'a': 1, 'b': 2}
print(a['a'])
print(a['b'])

dic = {'name': 'pey', 'phone': '0109993323', 'birth': '1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

# key 값이 같으면 (중복) 하나를 제외한 나머지 값이 무시
dic = {1: 'a', 1: 'b'}
print(dic)

# key 값에 리스트는 사용 불가
# dic = {[1,2]: 'hi'}

