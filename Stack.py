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
s=stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s.items)
print(s.pop())
print(s.items)
print(s.size())