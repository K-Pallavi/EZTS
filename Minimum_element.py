# find minimum element and put it on the start

l = list(map(int,input("Enter the numbers to be sorted:").split()))
target = l[0]
start = 0
for i in range(0,len(l)):
    if l[i] < target:
        target = l[i]
        start = target
        target +=1
print(start)
