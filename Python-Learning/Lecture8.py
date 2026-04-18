# OOP in Python
# To map with real world scenerios

# procedural programming --> functional --> Object Oriented

# Class & Object in Python
# Class is a blueprint for creating objects
# Car banane se phele uska blueprint ready hoga.. ki kya features hongey
# classes hum use nahi kr skte uske liye hume objects banane hongey

# creating object (instances of class)

class Car:
    color='blue'

car1 = Car() # constructor has been invoke/ python create by default
print(car1.color)

# Constructor (_init Function)
# All classes have a function called init() which is always executed when the class is being initiated
# jab bi koi new object create --> constructor has been invoke
# The self parameter is a ref to the current instance of the class
# attributes: name, variable
class Stu:
    # default constructor
    college= "MLVTEC"
    name = 'anonymous'
    def __init__(self):
        pass
    # parameterized constructor
    def __init__(self,fName): # object it self
        self.name = fName
        print("adding new student",self.name,self.college)

# whi constructor call hoga jo aapke parameter k sath match krrha h

s1 = Stu('vineet')
print()

s1 = Stu('nidhi')
print()
# CLASSES & INSTANCE ATTRIBUTES
# self.name (instance attribute) jo common nhi hoti uske liye
# college (class attribute) jo common hoti object k liye use hum class attribute bana dete h
# same name ka class & object attribue hota h to object attribute ki value aati h
# instance attribute Priority > class attribute

# METHODS (are functions that belongs to objects)
# class is basically collection of two things Attribute (var) & methods


class Std:
    def __init__(self,name, marks): # object it self
        self.name = name
        self.marks = marks
        print("adding new student",self.name)

    def welcome(self):
        print('Welcome student',self.name)
    
    def get_marks(self):
        return self.marks

s1 = Std('vineet',99)
s1.welcome()
print(s1.get_marks())

s2 = Std('nidhi',99)
s2.welcome()

# Create student class that make name & marks of 3 subjects as arguments in constructor. Then create a method to print the average

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sums = 0
        for val in self.marks:
            sums = sums+ val
        print(sums)
        print('average is',sums/3)

S1 = Student("vineet",[100,100,100])
S1.get_avg()

# STATIC METHODS (that don't use the self parameter work at class level)

class StaticMethods:
    @staticmethod #decorater
    def hello():
        print("hello")
ST = StaticMethods()
ST.hello()

# OOPS pillars
# 1. Abstraction 2. Encapsulation 3. Inheritance 4. Polymorphism

# Abstraction: Hiding the implementation details of a class any showing only the essential feature to the user

class Car:
    def __init__(self):
        self.acc = False
        self.clutch = False
        self.brake = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("car started")

C1 = Car()
C1.start()

# Encapsulation: Wrapping the data function into a single unit (object) eg: Car, Student use above

# Create Account class with 2 attributes - balance & account no.
# Create methods for debit, credit & printing the balance

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_number = acc
    
    # debit method
    def debit_bal(self, amount):
        self.balance = self.balance - amount
        print('Current balance is',self.get_balance())
    
    def credit_bal(self,amount):
        self.balance = self.balance + amount
        print('Current balance is',self.get_balance())
    
    def get_balance(self):
        return self.balance

acc1 = Account(1000,865686)
acc1.debit_bal(100)
acc1.credit_bal(10000)
print(acc1.account_number)