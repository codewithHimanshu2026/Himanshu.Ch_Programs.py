#1 WAP to check number is even or odd

'''a=int(input("Enter any number"))
if(a%2==0):
    print("Number is even")
else:
    print("Number is odd")'''

#2 WAP for 1st

'''l=[1,7,8]
for item in l:
        print(item)
else:
        print("done")'''


#3 WAP to check weekday name while user choice is 1-7

'''day=int(input("Enter a number "))
if(day==1):
    print("Monday")
elif(day==2):
    print("Tuesday")
elif(day==3):
    print("Wednesday")
if(day==4):
    print("Thrusday")
if(day==5):
    print("Friday")
if(day==6):
    print("Saturday")
if(day==7):
    print("Sunday")
else:
    print("Invalid choice")

a=[10,20]
a.append(30)
print(a)'''


'''a = ['Apple','Banana','cherry']
x = a.index("cherry")'''

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    result=factorial(5)
    print("Factorial=",result())