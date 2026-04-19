class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None 
root=Node(6)
a=Node(3)
b=Node(8)
root.right=a
root.left=b
print(root.data)
print(root.right.data)
