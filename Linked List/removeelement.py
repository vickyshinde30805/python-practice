# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):
        
        # Remove matching values from beginning
        while head and head.val == val:
            head = head.next
        
        current = head
        
        # Remove matching values from rest of list
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return head


# Helper function to create linked list from Python list
def create_linked_list(values):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    
    return head


# Helper function to print linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()


# Input from user
values = list(map(int, input("Enter linked list values: ").split()))
val = int(input("Enter value to remove: "))

# Create linked list
head = create_linked_list(values)

# Remove elements
solution = Solution()
new_head = solution.removeElements(head, val)

# Output result
print("Updated Linked List:")
print_linked_list(new_head)