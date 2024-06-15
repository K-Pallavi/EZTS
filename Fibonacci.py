#Fibonacci series
n=int(input("enter the number: "))
a=0
b=1
c=a+b
if n==1:
    print(a)
elif n==2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for i in range(2,n):
        print(c)
        a=b
        b=c
        c=a+b