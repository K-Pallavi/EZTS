class node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
        self.height=1

def insert(root,super):
    if not root:
        return node(super)
    if super<root.val:
        root.left=insert(root.left,super)
    else:
        root.right=insert(root.right,super)

    root.height=1+max(ght(root.left),ght(root.right))
    BF=getBF(root)
    #rr rotation
    if BF>1 and super<root.left.val:
        return rightRotate(root)
        
    #rl rotation
    if BF>1 and super>root.left.val:
        root.left=leftRotate()
        return rightRotate(root)
        
    #ll rotation
    if BF<-1 and super>root.right.val:
        return leftRotate(root)
        
    #lr rotation
    if BF<-1 and super<root.right.val:
        root.right=rightRotate(root.right)
        return leftRotate(root)
    return root

def ght(root):
    if not root:
        return 0
    return root.height

def getBF(root):
    if not root:
        return 0
    return ght(root.left)-ght(root.right)

def leftRotate(A):
    B=A.right
    temp=B.left
    B.left=A
    A.right=temp
    A.height=1+max(ght(A.left),ght(A.right))
    B.height=1+max(ght(B.left),ght(B.right))
    return B

def rightRotate(A):
    B=A.left
    temp=B.right
    B.right=A
    A.left=temp
    A.height=1+max(ght(A.left),ght(A.right))
    B.height=1+max(ght(B.left),ght(B.right))
    return B

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)
if __name__=="__main__":
    root=None
    vl=[20,18,5,16,23,26,39,37,22]
    for i in vl:
        root=insert(root,i)
    inorder(root)