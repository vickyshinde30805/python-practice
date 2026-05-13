# Data Structure Problem:
# Reverse a Linked List (VS Code Ready)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Insert node at end
def insert_at_end(head, data):
    new_node = Node(data)

    if head is None:
        return new_node

    temp = head
    while temp.next:
        temp = temp.next

    temp.next = new_node
    return head


# Reverse linked list
def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


# Print linked list
def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")


# Main
n = int(input("Enter number of nodes: "))

head = None

print("Enter node values:")
for _ in range(n):
    value = int(input())
    head = insert_at_end(head, value)

print("Original Linked List:")
print_list(head)

head = reverse_linked_list(head)

print("Reversed Linked List:")
print_list(head)