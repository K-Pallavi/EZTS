# Bubble sort
l=list(map(int,input("enter the elements to be sorted: ").split()))
for j in range(0,len(l)):
    for i in range(0,len(l)-1-j):
        if l[i]>l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
print(l)