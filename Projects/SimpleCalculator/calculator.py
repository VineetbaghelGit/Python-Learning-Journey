def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    if(b==0):
        return "Cannot divide by zero"
    return a/b


while True:
    print('\n 1. Add 2.Sub 3.Mul 4.Div 5.Exit')
    choice = input("Enter choice: ")

    if(choice == "5"):
        break

    a = float(input("enter first number: "))
    b = float(input("enter second number: "))

    if(choice =='1'):
        print(add(a,b))
    
    elif(choice =='2'):
        print(sub(a,b))

    elif(choice =='3'):
        print(mul(a,b))  

    elif(choice =='4'):
        print(div(a,b))
    else: print("invalid choice")

