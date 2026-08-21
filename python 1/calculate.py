def add():
    a=int(input("Enter any number"))
    b=int(input("Enter any number"))
    print("Addition=",a+b)

def sub():
    a=int(input("Enter any number"))
    b=int(input("Enter any number"))
    print("Addition=",a-b)

def multiply():
    a=int(input("Enter any number"))
    b=int(input("Enter any number"))
    print("Addition=",a*b)

def devide():
    a=int(input("Enter any number"))
    b=int(input("Enter any number"))
    print("Addition=",a/b)

while True:
    print("_____Calculator Program_____")
    print("1. Addition ")
    print("2. subtraction ")
    print("3. Multiplication ")
    print("4. Devide ")
    print("0. Exit ")

    choice=input("Enter any operation choose between 1-7")
    if choice=="1":
        add()
    elif choice=="2":
        sub()
    elif choice=="3":
        multiply()
    elif choice=="4":
        devide()
    elif choice=="0":
        print("____ThankYou____")
        break
    else:
        pass

    temp=input("Do you want to other operation yes/no").lower()
    if temp!="yes":
        print("----Thankyou----")
        break


