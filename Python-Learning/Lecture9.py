# del keyword
# Used to delete object properties or object itself

class Stu:
    # default constructor
    college= "MLVTEC"
    def __init__(self):
        pass
    # parameterized constructor
    def __init__(self,fName): # object it self
        self.name = fName
        print("adding new student",self.name,self.college)

# whi constructor call hoga jo aapke parameter k sath match krrha h

s1 = Stu('vineet')
del s1.name
# print(s1.name)
print()

# Private Attribute & Methods
# Private attribute & methods are meant to be used only within the class and are not accessible from outside the class

# class Account:
#     __name='anonymous'
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no= acc_no
#         self.__acc_pass= acc_pass # put __ make it private
    
#     def __show_password(self):
#         print('hello password')

# acc1 = Account('12345',"abcde")
# print(acc1.acc_no)
# print(acc1.show_password())
# print(acc1.__name)


# Inheritance: When one class derived the properties & methods of another class(parent/base)

class Car:
    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

# car1 = ToyotaCar("Fortuner")
# car2 = ToyotaCar("Innova")

# print(car1.start())

# Types of Inheritance
# 1. Single    2. Multi-level   3. Multiple

# Multi level (we can create level as much as we can)
class Fortuner(ToyotaCar):
    def __init__(self, type):
       self.type = type

car1 = Fortuner("diesel")
car1.start()

# Multi level (it could have many base classes)

class A:
    var_a = 'welcome to class A'

class B:
    var_b = 'welcome to class C'

class C(A,B):
    var_c = 'welcome to class C'
c1 = C()
print(c1.var_a,c1.var_b,c1.var_c)

# SUPER METHOD
# Super() method is used to access methods of the parent class

class CarNew:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("car started...")
    
    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCars(CarNew):
    def __init__(self,name,type):
        super().__init__(type)  #super use to call parent class 
        # because parent never called to uska object nh banege nd constructor will not invoked
        self.name = name
        super().start()

car1 = ToyotaCars('pirus','petrol')
print(car1.type)

# CLASS METHOD
# A class method is bound to the class & recieves the class as an implicit first argument
# Note: static method can't access or modify class state & generally for utility

class Person:
    name ="anonymous"

    # def changeName(self, name):
    #     self.name = name # only change here 
    #     # self.__class__.name = 'vineet'
    
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("vineet")
print(p1.name)  #vineet
print(Person.name) #anonymous

# PROPERTY

class Student:
    def __init__(self,phy,chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    # def calculate_percentage(self):
    #         self.percantage=  str((self.phy + self.chem+ self.math)/3)+ "%"
    
    # jab ek attribute ki value ek function pr depend krti h
    @property #decorater
    def percantage(self):
      return str((self.phy + self.chem+ self.math)/3)+ "%"

stu1 = Student(98,97,99)
print(stu1.percantage)
# stu1.phy=44
# stu1.calculate_percentage()
# print(stu1.percantage)
stu1.phy=44
print(stu1.percantage)

# POLYMORPHISM : Operator Overloading
# When the same operator is allowed to have different meaning according to the context

print(1+2) #add
print('vineet'+'baghel') #concatenate
print([1,2,3] + [4,5,6]) #merge

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def show_number(self):
        print(self.real,"i +", self.img,"j")
    
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg) 

num1 =Complex(1,3)
num2 =Complex(4,7)
num1.show_number()
num2.show_number()

# num3 = num1.add(num2)
# num3 = num2 + num1
num3 = num1- num2
num3.show_number()

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return (22/7) * self.radius ** 2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())

class Employee:
    def __init__(self, role,dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
    def show_details(self):
        print("role =",self.role )
        print("dept =",self.dept )
        print("salary =",self.salary )

class Engineer(Employee):
    def __init__(self, name, age,role,dept,salary):
        self.name = name,
        self.age =age
        super().__init__(role, dept, salary)

eng1 = Engineer("vineet", 27, "Engineer", "IT", 100000)
eng1.show_details()