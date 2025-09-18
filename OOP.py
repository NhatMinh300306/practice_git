#Object Oriented Programming in Python
#Phải luôn có self: đại diện cho đối tượng (instance) hiện tại của lớp và cho phép truy cập vào các thuộc tính cũng như phương thức của đối tượng đó.

class Dog:
	#init ~ Constructor: Tự động được gọi khi khai báo đối tượng
	def __init__(self, name, age):
		self.name = name #Tạo attribite tên là "name" - Không cần khai báo trước
		self.age = age #thêm _vào trước tên attribute để hiểu đây là private

	def get_name(self): #getter
		return	self.name

	def get_age(self):
		return self.age

	def set_age(self, age): #setter
		self.age = age

	def set_name(self):
		self.name = name

	def bark(self): #method
		print("bark")

d = Dog("Tim", 18)
#print(d.name) # đối tượng có thể truy cập vào attribute bên ngoài class nếu public
print(d.get_name())
print(d.get_age())

print("")

d2 = Dog("Bill", 19)
#print(d2.name): lỗi do phạm vi truy cập là private, không phải public
print(d2.get_age())
d2.set_age(20)
print(d2.get_age())

d.bark()
print(type(d))
print("")

#---------------------------------------------
class Student:
	def __init__(self, name, age, grade):
		self.name = name 
		self.age = age 
		self.grade = grade

	def get_grade(self):
		return self.grade

class Course:
	def __init__(self, name, max_students):
		self.name = name 
		self.max_students = max_students
		self.students = []

	def add_student(self, student):
		if len(self.students) < self.max_students:
			self.students.append(student)
			return True
		return False

	def get_average_grade(self):
		value = 0
		for student in self.students:
			value += student.get_grade()
		return value / len(self.students)

s1 = Student("Tim", 19, 9)
s2 = Student("Bill", 19, 8)
s3 = Student("Sarah", 19, 7)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
#nếu add(s3): lỗi vì course chỉ có thể nhận 2 student như đã khai báo
print(course.students[0].name)
print(course.get_average_grade())
print("")
#----------------------------------------------------------
#Inheritance
class Pet:
	def __init__(self, name, age):
		self.name = name 
		self.age = age 

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old")

	def speak(self):
		print("I don't know what I say")

class Cat(Pet):
	def __init__(self, name, age, color):
		super().__init__(name, age) #super: a function used in a child class to call methods from a parent class
		self.color = color
		#Cách khác: 
		'''
		self.name = name 
		self.age = age
		'''
		
	def speak(self):
		print("Meow")

	def show(self):
		print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Chicken(Pet): #Kế thừa
	def speak(self):
		print("Quack")

class Fish(Pet):
	pass #dùng để đánh dấu một vị trí trong code mà không thực hiện bất kỳ hành động nào
	#Trong oop nếu dùng pass: thì khi gọi đến 1 method nào đó thì nó sẽ dụng method của lớp cha

p = Pet("Eren", 17)
p.show()
p.speak()

c = Cat("Mikasa", 17, "white")
c.show()
c.speak()

ch = Chicken("Armin", 17)
ch.speak()

f = Fish("Nika", 17)
f.speak()
print("")
#--------------------------------------------------------
#Class Attribute
class Person:
	number_of_people = 0

	def __init__(self, name):
		self.name = name 
		Person.add_person()
		#Hoặc: Person.number_of_people += 1
	@classmethod #decorator trong Python dùng để xác định một phương thức là phương thức lớp (class method) thay vì phương thức của đối tượng
	def number_of_people_(cls): #cls:  là một tham số thường được sử dụng trong phương thức lớp (class method) để tham chiếu đến chính lớp đó, thay vì một đối tượng cụ thể như self
		return cls.number_of_people

	@classmethod
	def add_person(cls):
		cls.number_of_people += 1

p1 = Person("Shiro")
p2 = Person("Kuro")

print(p1.number_of_people)
print(Person.number_of_people) #có thể dùng tên class để gọi
print(Person.number_of_people)

#Person.number_of_people = 8 #thay đổi giá trị
#print(p2.number_of_people)

print(Person.number_of_people_())
print("")

#----------------------------------------------------
#Static methods
'''
- A method that belong to a class rather than any object from that class
- Best for utility functions that do not need access to class data
'''
class Math:
	@staticmethod
	def add5(x):
		return x + 5

	@staticmethod
	def add10(x):
		return x + 10

	@staticmethod
	def pr():
		print("run")

print(Math.add5(5))
Math.pr()
print("")
#---------------------------------------------------------------
#Math operator
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): # +; __sub__ cho trừ và __mul__ cho nhân
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self): #__str__: chuyển đổi tượng thành chuỗi khi dùng print
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)  # Kết quả: Vector(6, 8)
print(v1.__add__(v2))
#tự động gọi đến __add__ thay vì v1.__add__(v2) và vì __add__ đã có return

#----------------------------------------
#Multiple Inheritance
class Animal:
	def __init__(self,name):
		self.name = name
	def eat(self):
		print(f"This {self.name} is eating")
	def sleep(self):
		print("This animal is sleeping")
class Prey(Animal):
	def flee(self):
		print(f"{self.name} is fleeing")
class Predator(Animal):
	def hunt(self):
		print("This animal is hunting")
class Rabbit(Prey):
	pass 
class Hawk(Predator):
	pass
class Fish(Prey, Predator):
	pass 

rabbit = Rabbit("Bugs")
rabbit.flee()
#Abstract Class
'''
- A class that cannot be instantiated on its own; Meant to be subclassed
- They can contain abstract methods, which are declared but have no implementatiion
- Benefits:
1. Prevents intantiation of class itself
2. Requires children to use inherited abstract methods
'''
from abc import ABC, abstractmethod #to use abstractmethod

class Vehicle(ABC): #Declare abstract class
	@abstractmethod
	def go(self):
		pass
	def stop(self):
		pass 

class Car(Vehicle):
	def go(self):
		print("You drive the car")
	def stop(self):
		print("You stop the car")

car = Car()
car.go()
car.stop()
print()


#Nested class = A class defined within another class
#              class Outer:
#                   class Inner:
#Benefit:
#- Allows you to locally group classes that are closely related
#- Encapsulates private details that aren't relevant outside of the outer class
#- Keeps the namespace clean; reduce the possibility of naming conflicts
class Company:
	class Employee:
		def __init__(self, name, position):
			self.name = name
			self.position = position

		def get_details(self):
			return f"{self.name} {self.position}"

	def __init__(self, company_name):
		self.company_name = company_name
		self.employees = []

	def add_employee(self, name, position):
		new_employee = self.Employee(name, position)
		self.employees.append(new_employee)

	def list_employee(self):
		return [employee.get_details() for employee in self.employees]

company = Company("Krusty Crab")
company.add_employee("Steve", "Manager")
company.add_employee("Spongebob", "Cook")
for employee in company.list_employee():
	print(employee)