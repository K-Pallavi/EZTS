class node:
    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None
def insert_bst(root,value):
    if root==None:
        return node(value)
    if value<root.value:
        root.left=insert_bst(root.left,value)
    if value>root.value:
        root.right=insert_bst(root.right,value)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)
list=[4,6,7,3,8,2,5,9,1]
root=node(list.pop(0))
for i in list:
    insert_bst(root,i)
inorder(root)
    

   