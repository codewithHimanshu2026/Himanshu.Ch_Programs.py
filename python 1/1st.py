        #1 WAP to find sum of two numbers 

'''a=int(input("Enter any number"))
b=int(input("Enter any number"))
sum=a+b
print("Sum of a and b are",sum)'''

        #2 WAP to find Area of circle

'''r=int(input("Enter circle radius"))
Area=3.14*r*r
print("Area of circle is ",Area)'''

        #3 WAP to swap two numbers using 3rd variable

'''a=int(input("Enter any number"))
b=int(input("Enter any number"))
print("value of a and b before swapping",a,b)
c=a
a=b
b=c
print("value of a and b after swapping.",a,b)'''

        #4 WAP to swap two number without using 3rd variable

'''a=int(input("Enter any number"))
b=int(input("Enter any number"))
print("value of a and b before swapping",a,b)
a=a+b
b=a-b
a=a-b
print("value of a and b after swapping",a,b)'''

        #5 WAP to convert celcius into Fernhite

'''celcius=float(input("Enter temp in celcius"))
Fehrenhiet=(celcius*9/5)+32
print("Temperature in Fehrenhiet",Fehrenhiet)'''

        #6 WAP to find area of triangle

'''b=int(input("Enter base of triangle"))
h=int(input("Enter height of triangle"))
Area=1/2*b*h
print("Area of triangle is",Area)'''

        #7 WAP to calculate the percentage of five subjects

'''a=int(input("Enter your Hindi marks"))
b=int(input("Enter your English marks"))
c=int(input("Enter your Maths marks"))
d=int(input("Enter your Physics marks"))
e=int(input("Enter your Chemistry marks"))
percentage=(a+b+c+d+e)/5
print("total percentage is",percentage)'''

        #8 WAP to calculate square and cube of any number

'''n=int(input("Enter any number"))
square=n*n
cube=n*n*n
print("The square of number is ",square)
print("The cube of number is ",cube)'''


        #11 WAP to check character is a number,Alphabet,Vowels,Special-symbol,etc

'''ch=input("Enter any character")
if(ch>="0" and ch<="9"):
    print("Enter character is a Number")
if((ch>="a" and ch<="z") or (ch>="A" and ch<="Z")):
        if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U" ):
             print("Enter Character is a Alphabet or Vowel")
        else:
             print("Enter character is a Alphabet")
else:
     print("Enter character is a Special-symbol")'''

        #12 WAP to check Bigger number in two numbers

'''a=int(input("Enter any number"))
b=int(input("Enter any number"))
if(a>b):
      print("A is greater:",a)
if(b>a):
      print("B is Bigger:",b)
if(a==b):
      print("a and b both are bigger ")'''

        #13 WAP to sum of numbers in for loop.

'''sum=0
a=int(input("Enter any number"))
for i in range(1,10):
    sum=sum+i
    print("Sum=",sum)'''

        #14 WAP to check Bigger number using if-else

'''a=int(input("Enter any number"))
b=int(input("Enter any number"))
if(a>b):
    print("a is bigger",a)
else:
    print("b is greater",b)'''

        #15 WAP to check given number is positive or negative.

'''n=int(input("Enter any number"))
if(n>=0):
    print("Number is +ve")
else:
    print("Number is -ve")'''

        #16 WAP to check number is divisible by 5.

'''n=int(input("Enter any number"))
if(n%5==0):
    print("Enter number is divisible by 5")
else:
    print("Number is not divisible by 5")'''

        #17 WAP to find HCF and LCM of two number

'''a=int(input("Enter any number"))
b=int(input("Enter any number"))
c=min(a,b) 
for i in range(1,c+1,1):
    if a%i==0 and b%i==0:
        hcf=i
lcm=(a*b)/hcf
print("LCM=",lcm, "HCF=",hcf)'''

        #18 WAP to find factorial of any number

'''a=int(input("Enter any number"))
fact=1
for i in range(1,a+1,1):
    fact=fact*i
print("Factorial=",fact)'''

        #19 WAP to create an Table of any number

'''n=int(input("Enter any number"))
for i in range(1,11):
        print(n,"X",i,"=",n*i)'''

         
        #20 WAP to sum of all numbers

'''sum=0
n=int(input("Enter any number"))
for i in range(1,n+1,1):
        sum=sum+i
        print("Sum=",sum)''' 

        #21 WAP to reverse a any number

'''n=int(input("Enter any number"))
temp=n
r=0
rev=0
length=len(str(n))
for i in range(1,length+1,1):
        r=n%10
        rev=rev*10+r
        n=n//10
print("Reverse value=",rev)
if(temp==rev):
        print("Number is Palindrome")
else:
        print("Number is not a palindrome")'''


        #22 WAP to create a Fibonacci series.

'''n=int(input("Enter any number"))
n1=0
n2=1
for i in range(1,n+1,1):
        print(n1,end=" ")
        n3=n1+n2
        n1=n2
        n2=n3'''
        
        
        #23 WAP to create a Tribonacci series
         
'''n=int(input("Enter any number"))
n1=0
n2=0
n3=1
for i in range(1,n+1,1):
        print(n1,end=" ")
        n4=n1+n2+n3
        n1=n2
        n2=n3
        n3=n4'''

        #24 WAP to create a A-Z write.


'''for i in range(65,91):
        print(chr(i),end=" ")
        print()'''

        #25 1.WAP to create an pattern
 
'''for i in range(1,6):
        for j in range(1,6):
                print("*",end=" ")
        print() '''

            #2.WAP to create a pattern

'''for i in range(1,6):
        for j in range(1,i+1):
                print("*",end=" ")
        print()'''

                #3.pattern

'''for i in range(1,6):
        for j in range(5,i,-1):
                print(" ",end=" ")
        for j in range(1,i+1):
                print("*",end=" ")
        print()'''

                #4.pattern

'''for i in range(1,6):
        for j in range(6,i,-1):
                print("*",end=" ")
        for j in range(1,i+1):
                print(" ",end=" ")
        print()'''

                #5.pattern



                #6.pattern (T)

'''for i in range(1,6):
        for j in range(1,6):
                if(i==1 or j==3):
                        print("*",end=" ")
                else:
                        print(" ",end=" ")
        print()'''

                #7.pattern

'''for i in range(1,6):
        for j in range(5,i,-1):
                print(" ",end=" ")
        for j in range(0,2*i-1):
                print("*",end=" ")
        print()'''

                #8.pattern

'''for i in range(1,6):
        for j in range(1,i+1):
                print(" ",end=" ")
        for j in range(6,i,-1):
                print("*",end=" ")
        print()'''

                #9.pattern (X)

'''for i in range(1,6):
        for j in range(1,6):
                if(i==j or i+j==6):
                        print("*",end=" ")
                else:
                        print(" ",end=" ")
        print()'''


                #10.pattern

'''n=1
for i in range(1,6):
        for j in range(1,i+1,1):
                print(n,end=" ")
                n=n+1
        print()'''


                #11.pattern (A)x

'''for i in range(1,6):
        for j in range(5,i,-1):
                print(" ",end=" ")
        for j in range(0,2*i-1,1):
                if(i==j or i==3 or i==2 and j==6 or i==3 and j==7 or i==4 and j==8 or i==5 and j==9):
                        print("*",end=" ")
        print()'''


                #12.pattern

'''for i in range(1,6):
        for j in range(1,i+1):
                print(j,end=" ")
        print()'''


                #13.pattern

'''for i in range(1,6):
        for j in range(1,6):
                if(j==1 or i==1 and i!=4 and i!=5 or i==2 and j==4 or i==3 and j==3 or i==4 and j==4 or i==5 ):
                        print("*",end=" ")
                else:
                        print(" ",end=" ")
        print()'''


                #14.pattern

'''for i in range(1,6):
        n=i
        m=4
        for j in range(1,i+1):
                print(n,end=" ")
                n=n+m
                m=m-1
        print()'''


        #15.pattern

'''for i in range(1,9):
        for j in range(1,5):
                if(i==1 and (j>1 and j<4) or i==8 and (j>1 and j<4) or i==2 and (j!=2 and j!=3) or i==7
                   and (j!=2 and j!=3) or i==3 and j==1 or i==6 and j==4 or i==4 and j==2 or i==5 and j==3):
                        print("*",end=" ")
                else:
                        print(" ",end=" ")
        print()'''



                #26 WAP check number is Armstrong number

'''n=int(input("Enter any number"))
l=len(str(n))
temp=n
arm=0
for i in range(1,l+1):
        r=n%10
        arm=arm+r**l
        n=n//10
if(temp==arm):
        print("Enter number is a Armstrong")
else:
        print("Enter number is not a Armstrong")'''


                #27 WAP to find 1000 Armstrong number

'''n=1
while(n<=1000):
        l=len(str(n))
        arm=0
        temp=n
        for i in range(1,l+1):
                r=temp%10
                arm=arm+r**l
                temp=temp//10
        if(n==arm):
                print(n)
        n=n+1'''

                #28 WAP to LIST

'''l=[1,2,3]
print(l[-1])

print(l[0:2])

print(l.append(4),l)



l=[1,2,3,6]
print(l.extend([21,23]),l)

l=[1,2,3,5]
print(l.remove(2),l)

l=[1,2,3,7]
l.pop()
print(l)

l=[1,2,3,3]
del l[0]
print(l)

l=[1,2,2,3]
l.clear()
print(l)

l=[1,1,22,3,5,3,6,99,4]
l.sort()
print(l)

l=[1,2,3,11]
l.reverse()
print(l)

l1=[1,2,3,]
l2=[4,77]
l3=l1+l2
print(l3)
'''

'''a=[1,2,3,4,33]
v=a*2
print(v)


l=[1,2,3,4]
l.insert(1,100)
print(l)

a=[1,2,3,4]
a.pop(1)
print(a)

b=[1,2,3]
print(len(b))

c=[10,20,30,30]
print(c.count(30))

s=[11,2,3]
s.sort(reverse=True)
print(s)

k=[1,2,2,33]
print(2 in k)

l=[1,2,3,44]
for i in l:
        print(i)'''



                #29 WAP to STRING

'''a="Himanshu"
print(a.upper())

v="india"
print(v.title())

f="Naruto"
print(f.capitalize())

b='SaSkE'
print(b.swapcase())

w="I am Kakashi"
print(w.replace("Kakashi","Perry"))

g="Youth"
print(g.find("u"))

j="Akamaro"
print(j.count("a"))

i="Lokism","Anime"
print("_".join(i))

#start and end both. same
l="Sun-Pharma"
print(l.startswith("Sun"))

r="Dude"
print(r.isalnum())

#Upper and Lower Both.
t="Himanshu"
print(t.isupper())

v='Hello'
print(v.isalpha())

w='Welcome'
print(w.isdigit())

a='Naruto'
print(a.split())

c="Hello"
print(c.isalnum())

p='44'
print(p.zfill(4))

d='     JAAT     '
print(d.strip())

y="Ayono"
print(y.center(50,"*"))'''


                #30 Program

'''def add():
    a=5
    b=5
    c=a+b
    print("Answer=",c)'''
    


                #31 program.

'''def add():
    a=12
    b=12
    c=a+b
    return c
print("Answer=",add())'''


                #32 program.

'''def add(a,b):
    c=a+b
    print("Answer=",c)

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
add(a,b)'''


                #33.program

'''def add(a,b):
    c=a+b
    return c
a=5
b=5
print("ans=",add(a,b))'''


                #34.program fact

'''def fact(x):
    f=1
    if x==0 or x==1:
        return 1
    else:
        f=x*fact(x-1)
        return f
n=int(input("Enter any number"))
print("Factorial=",fact(n))'''


                #35.program fib

'''def fib(x):
        if x==0 or x==1:
                return 1
        else:
              return fib(x-1)+fib(x-2)
        
        n=int(input("Enter any number"))
        for i in range(n):
               print(fib(i),end=" ")'''


                #36.program

'''class A():
    def show(self):
        print("show")

class B(A):
    def view(self):
        print("view")

class C(A):
    def display(self):
        print("display")

obj1=A()
obj2=B()
obj3=C()

obj2.view()
obj3.display()
obj1.show()

obj2.show()
obj3.show()'''


                #37.program lib

'''import math
print(math.sqrt(5))

print(math.factorial(5))

print(math.ceil(2.5))

print(math.pow(9,2))

print(math.isfinite(11))

print(math.floor(6.6))'''


                #38.program

'''try:
    a=int(input("Enter any number"))
    b=0
    print(a/0)
except ZeroDivisionError:
    print("Number cannot divided by zero")
except ValueError:
    print("please enter the valid number")

finally:
    print("Program run successfully")'''


                #39 program age in VOTE

'''try:
    a=int(input("Enter Your age"))

    if a<0:
        raise ValueError("Age cannot be a negative")
    if a>=18:
        print("You are eligible for voting")
    else:
        print("You are not eligible for VOTE")

except ValueError as hii:
    print("Invalid input",hii)

finally:
    print("Program run successfully")'''


                #40.program

'''file=open("abc.txt","x")
file.close()
file=open("abc.txt","")'''

                #41 program FILE HANDL

'''file=open("abc.txt","w")
file.write("HII I am Himanshu")
file.close()'''

'''file=open("abc.txt","a")
file.write("Add Director.")
file.close()'''

'''file=open("abc.txt","r")
print(file.readline())
file.close()'''

'''with open("abc.txt","r")as file:
    print(file.read())'''

'''with open("abc.txt","a")as file:
    n=input("Enter your name")
    file.write(n+"\n")
    file.close()'''

'''with open("abc.txt","+a")as file:
    n=(input("Enter your name"))
    file.write(n)
    file.close()'''

#42 search the word in txt file 

'''search=input("Enter any word did you search.")
with open("abc.txt","r")as file:
    data=file.read()
if search in data:
    print("word are found")
else:
    print("Word are not found")'''


#43 CSV.

'''import csv
with open("Student.csv","w",newline="") as file:
    writer =csv.writer(file)
    writer.writerow(["name","roll.no","PRJ No."])
    writer.writerow(["Himanshu",22,343])
    writer.writerow(["jhih",89,988])
    writer.writerow(["jaiufd",29,909])'''





