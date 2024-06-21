arr=[5,7,-10,-3,0,3,-5,1]
min=arr[0]
for i in range(1,len(arr)):
    if arr[i]<arr[0]:
        min=arr[i]
print(min)