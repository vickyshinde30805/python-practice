class Node:
     def __init__(self,data):
          self.data=data
          self.next=None

def printLL(head):
    curr=head
    while curr!=None:
         print(curr.data,end=" ")
         curr=curr.next
    print()

# Create linked list
a=Node(5)
b=Node(7)
c=Node(2)
a.next=b
b.next=c
head=a

# Insert at beginning
newNode=Node(3)
newNode.next=head
head =newNode

#insert at the end
endNode=Node(8)
curr=head
while curr.next!=None:
     curr=curr.next
curr.next=endNode

#insert at the middle
middleNode=Node(9)
k=4
curr=head
for i in range(k-2):
     curr=curr.next
middleNode.next=curr.next
curr.next=middleNode


printLL(head)