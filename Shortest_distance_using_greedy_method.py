# Shortest Distance using greedy method
M=[[1,2,2,3],
   [3,1,4,2],
   [1,5,3,3],
   [1,2,1,1]]
n=len(M)-1
m=len(M[0])-1
i=j=0  
sum=M[i][j]
while(i<n or j<m):
    if i==n:
        j+=1
    elif j==m:
        i+=1
    elif M[i][j+1]<M[i+1][j]:
        j+=1
    else:
        i=i+1
    sum+=M[i][j]
print(sum)
