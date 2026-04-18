# Functions in Python
# Block of statement that perform a specific task

#function definition
def calc_sum(a,b): #parameters
    return a+b

print(calc_sum(5,6)) #function call, agruments
print(calc_sum(7,7))
print(calc_sum(8,9))

def cal_avg(a,b,c):
    sums = a+b+c
    avg = sums/3
    return avg

print(cal_avg(5,10,20))

# Types of Function
# In Built Function: range(), len(), type(), print()

# User defined Function

# Default Parameters

def cal_prod(a=1,b=1):
    mult = a*b
    return mult

print(cal_prod(4,5))

# WAP to print the length of a list (list is a parameter)
cities = ['delhi', 'mumbai','chennai', 'bhilwara','pune']

def print_len(list):
    print(len(list))

print_len(cities)    

# WAP to print the elements of a list in a single line

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(cities)

# WAP to find the factorial of n


def cal_fact(n):
    fact =1 
    for i in range(1, n+1):
        fact *= i
        print(fact)

cal_fact(5)

# WAP even odd 

def cal_odd_even():
    val = int(input("enter number"))
    if(val%2 == 0):
        print("EVEN")
    else:
        print("ODD")

cal_odd_even()

# RECURSION: When a function call itself repeatedly

def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)

# Factorial

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
    
print("fact",fact(4) )   

# WAP to calculate the sum of first n natural numbers using Recursion

def cal_sum_rec(n):
    if(n==0): return 0
    return n + cal_sum_rec(n-1)

print('cal_sum_rec',cal_sum_rec(5))

# WAP to print all element in a list using recursion
listLang = ["python", 'Java','C++', "python", 'JS',"C++","C","Java","JS"]
def print_list_rec(l,idx=0):
    if(idx==len(l)):
        return
    print(l[idx])
    print_list_rec(l,idx+1)

print("print_list_rec",print_list_rec(listLang))