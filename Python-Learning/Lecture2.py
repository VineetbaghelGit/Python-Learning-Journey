# Conditional statement
# for single apostrope we use triple quote

str1 = 'this is a string. \n we are creating in python'
print(str1)
print(len(str1))
print(str1[0])
# str1[3] = 'a' #'str' object does not support item assignment

# SLICING
print(str1[1:6])
print(str1[1:])
print(str1[:5])

# negative Index starting with -1(from backward) and so on
str2 = "Apple"
print(str2[-5:-1])

# Strings functions
str3 = 'i am currently studying python'
print(str3.endswith('python'))
print(str3.capitalize()) #did not modify original string
print(str3.replace('currently','abhi'))
print(str3.find('currently'))
print(str3.count('i'))

# WAP
# name = input('enter your name')
# print(len(name))

# Conditional Statment

# if - elif - else

age = 16

if(age >= 18):
    print('Can vote')
else: print("not eligible")

# WAP grade student

mark = 70

if(mark >=90):
    print("A")
elif(90 > mark and mark >=80):
    print("B")
elif(80 >mark and mark>= 70):
    print("C")
else: print("D")

# WAP 
num = int(input('enter number'))
rem = num % 2
if(rem ==0):
    print('Even')
else: print("ODD")