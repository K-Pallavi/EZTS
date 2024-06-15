""" Given an integer array your task is to find the 3 continuous digits which gives you the maximum sum
sample input
[2,4,3,5,6,3,4,6,7,1,2,5]
output:[4,6,7]"""
l=[2,4,3,5,6,3,4,6,7,1,2,5]
sum=max=0
for i in range(0,len(l)-2):
    sum=l[i]+l[i+1]+l[i+2]
    if max<sum:
        max=sum
        pos=i
print(max,l[pos],l[pos+1],l[pos+2])