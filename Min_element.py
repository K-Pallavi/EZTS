# searching for min element
l=list(map(int,input("enter the elements: ").split()))
min=l[0]
for i in range(0,len(l)):
    if l[i]<min:
        min=l[i]
print("the minimum element is: ",min)