# Merge K Sorted Linked Lists using Array Method
# For VS Code (with input + output)

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


# Function to create linked list from array
def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


# Function to merge k lists
def mergeKLists(lists):
    arr = []

    # Step 1: Store all values in array
    for head in lists:
        while head:
            arr.append(head.val)
            head = head.next

    # Step 2: Sort array
    arr.sort()

    # Step 3: Convert array back to linked list
    dummy = ListNode(0)
    current = dummy

    for num in arr:
        current.next = ListNode(num)
        current = current.next

    return dummy.next


# Function to print linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


# Main Code
k = int(input("Enter number of linked lists: "))

lists = []

for i in range(k):
    arr = list(map(int, input(f"Enter sorted elements of list {i+1}: ").split()))
    lists.append(create_linked_list(arr))

# Merge all lists
result = mergeKLists(lists)

# Output
print("Merged Sorted Linked List:")
print_linked_list(result)