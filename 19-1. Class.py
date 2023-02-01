# class.py
class Calculartor:
	def __init__(self):
		self.result = 0

	def adder(self, num):
		self.result += num
		return self.result

cal1 = Calculartor()
cal2 = Calculartor()

print(cal1.adder(3))
print(cal1.adder(4))

print(cal2.adder(3))
print(cal2.adder(7))


# 껍데기만 있는 클래스
class Simple:
	pass

class Service:
	secret = '영구는 배꼽이 두개다.'

	# Constructor
	def __init__(self, name):
		self.name = name

	def sum(self, a, b):
		result = a + b
		print("%s님 %s + %s = %s입니다." % (self.name, a, b, result))

pey = Service("홍길동")
print(pey.secret)
# pey.setname("홍길동")
pey.sum(1, 1)


class FourCal:

	def __init__(self, first, second):
		self.first = first
		self.second = second

	def sum(self):
		return self.first + self.second

	def sub(self):
		return self.first - self.second

	def mul(self):
		return self.first * self.second

	def div(self):
		return self.first / self.second

a = FourCal(4, 2)
print(a.sum())
print(a.sub())
print(a.mul())
print(a.div())


class HousePark:
	lastName = "정"

	def __init__(self, name):
		self.fullName = self.lastName + name

	def travel(self, where):
		print("%s, %s여행을 가다." % (self.fullName, where))

a = HousePark("재오")
a.travel("부산")

# 인자를 받으면 상속!!
class HouseKim(HousePark):
	lastName = "김"

	def travel(self, where, day):
		print("%s, %s여행 %s 가네" % (self.fullName, where, day))

b = HouseKim("줄리엣")
b.travel("독도", 3)