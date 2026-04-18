# LOOPS

# Loops are used to repeat instructions
# While & For Loop

# Kisi variable ki value update krna hoto while stoping condition ho

count = 1 # Iterator

while count <= 5:
    print("hello")
    count +=1

# 1 to 100
i = 1
while i <= 100:
    print(i)
    i +=1


# 100 to 1
j = 100
while j >=1:
    print(j)
    j -=1

# Table
# k = 1
# n = int(input("enter number"))
# while k <= 10:
#     print(n*k)
#     k +=1

nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx +=1

# Search for a number X in this tuple using loop
x = 100
nums = (1,4,9,16,25,36,49,64,81,100)
id = 0
while id <= len(nums):
    if(nums[id] == x): 
        print('Found at idx',id)
        break
    id +=1

# BREAK: Break the loop
# CONTINUE: Skip the current iteration only and continue from next again 

# FOR LOOPS: USED FOR SEQENTAIL TRAVERSAL

listNum = [1,2,3,4,5]

for val in listNum :print(val)

tupleNum = (1,2,3,45,6,9)

for el in nums: print("for loops",el)

# RANGE: Range function returns a sequence of numbers, Starting from 0 by default and increments by 1 (by default) and stops before a specified number

# range(start?, stop, step?)
# seq = range(5)
seq = range(2,10,2)
for i in seq: print('range',i)

for i in range(100,0,-1): print(i)

# Pass statement: When you want something that does nothing

for i in range(5):
    pass

# WAP to find the sum of first n numbers

n = 5
total = 0
vari = 1
while vari <= n:
    total += vari;
    vari += 1

print(total)

# WAP to find facotrial of first n numbers

nF = 5

fact = 1
for el in range(1,nF+1): 
    fact = fact * el

print(fact)    