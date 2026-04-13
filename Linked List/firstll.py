class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=Node(5)
b=Node(7)
c=Node(2)
a.next=b
b.next=c
head=a

print(head.data,end=" ")
print(head.next.data,end=" ")
print(head.next.next.data,end=" ")

