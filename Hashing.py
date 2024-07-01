k = [22,10,47,56,100,50,92,99,79]  
hashList = [False for _ in range(10)]
print(hashList)
for e in k:
    for j in range(len(k)):
        x=((e%10)+j)%10
        if hashList[x]==False:
            hashList[x]=e
            break

print(hashList)
