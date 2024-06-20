# BFS by using Queue(left view)
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
        
def levelorder(root):
    Q=[root]
    Q.append(None)
    print(root.value)
    
    while len(Q)>0:
        curr=Q.pop(0)
        if curr==None:
            if len(Q)==0:
                return
            else:
                print(Q[0].value)
                Q.append(None)

                
        else: 
            if curr.left !=None:
                Q.append(curr.left)
            if curr.left !=None:
                Q.append(curr.right)
                
                
                
    
if __name__=="__main__":
    root = node(1)
    
    root.left=node(2)
    root.right=node(3)
    
    root.left.left=node(4)
    root.left.right=node(5)
    
    root.right.left=node(6)
    root.right.right=node(7)
    
    levelorder(root)
