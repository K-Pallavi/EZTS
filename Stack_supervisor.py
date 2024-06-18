'''Input:[3,5,2,14,5,3,7,9,4,6,9,4,2,5,3]
   output:[15,14,14,-1,7,7,9,-1,6,9,-1,5,5,-1,-1]'''
class stack:
    def __init__(self):
        self.items=[]

    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
        
    def top(self):
        return self.items[-1]
        
inp=[3,5,2,14,5,3,7,9,4,6,9,4,2,5,3]
s=stack()
l=[0]*len(inp)
for i in range(len(inp)-1,-1,-1):
    if s.size()!=0:
        while s.size()!=0 and s.top()<inp[i]:
            if s.top()<inp[i]:
                s.pop()
    if s.size()==0:
        l[i]=-1
    else:
        l[i]=s.top()
    s.push(inp[i])
print(l)