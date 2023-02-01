# List Function.py

# append: 뒤에 요소 추가
a = [1, 2, 3]
a.append(4)
print(a)

# append: 뒤에 리스트 추가
a.append([5, 6])
print(a)

# 정렬
list = [1, 4, 3, 2]
list.sort()
print(list)

list = ['a', 'b', 'c']
list.reverse()
print(list)

# index: 값을 찾아서 index 리턴
# 값이 없으면 오류 발생
a = [1, 2, 3]
print(a.index(3))
print(a.index(1))

# insert: 값 삽입 > index, value
a = [1, 2, 3]
a.insert(0, 4)
print(a)

a.insert(3, 5)
print(a)

# remove : 왼쪽부터 찾아서 나오는 첫번째 값 삭제
a = [1, 2, 3] * 2
a.remove(3)
print(a)

a.remove(3)
print(a)

# pop: 요소 끄집어내기
a = [1, 2, 3]
print(a.pop())
print(a)

# index 지정
a = [1, 2, 3]
print(a.pop(1))
print(a)

# count: 리스트 내 x가 몇개 있는지
a = [1, 2, 3, 1]
print(a.count(1))

# extend: 리스트 확장 (리스트만 가능)
a = [1, 2, 3]
a.extend([4, 5])
print(a)

b = [6, 7]
a.extend(b)
print(a)

