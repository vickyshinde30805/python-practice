# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        
        pointerA = headA
        pointerB = headB
        
        # Traverse both lists
        while pointerA != pointerB:
            
            # Move pointerA
            if pointerA:
                pointerA = pointerA.next
            else:
                pointerA = headB
            
            # Move pointerB
            if pointerB:
                pointerB = pointerB.next
            else:
                pointerB = headA
        
        return pointerA


# Helper function to create linked list
def create_linked_list(values):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    
    return head


# Helper function to get node at specific position
def get_node(head, pos):
    current = head
    for _ in range(pos):
        if current:
            current = current.next
    return current


# Helper function to print linked list
def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()


# Input first list
listA = list(map(int, input("Enter first linked list: ").split()))

# Input second list
listB = list(map(int, input("Enter second linked list: ").split()))

# Create separate lists
headA = create_linked_list(listA)
headB = create_linked_list(listB)

# Optional intersection position
choice = input("Do you want to create intersection? (yes/no): ").lower()

if choice == "yes":
    posA = int(input("Enter position in first list where second list should intersect: "))
    
    intersection_node = get_node(headA, posA)
    
    if intersection_node:
        current = headB
        while current.next:
            current = current.next
        current.next = intersection_node


# Print lists
print("Linked List A:")
print_list(headA)

print("Linked List B:")
print_list(headB)


# Find intersection
solution = Solution()
result = solution.getIntersectionNode(headA, headB)

# Output
if result:
    print("Intersection at node value:", result.val)
else:
    print("No intersection found")