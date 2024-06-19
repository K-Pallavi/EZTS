class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
Head=Tail=Node(10)
#Head.next=Node(20)
#Head.next.next=Node(30)
Tail.next=Node(20)
Tail=Tail.next
Tail.next=Node(30)
Tail=Tail.next
Tail.next=Node(40)
Tail=Tail.next
print(Head)
print(Tail)
print(Head.next.next.next)