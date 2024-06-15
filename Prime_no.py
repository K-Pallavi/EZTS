n=int(input("enter the number: "))
flag=0
if n<0:
    flag=1
elif n==0:
    flag=0
else:
    for i in range(2,n):
        if n%i==0:
            flag=1
            break
if flag==0:
    print("valid")
else:
    print("invalid")