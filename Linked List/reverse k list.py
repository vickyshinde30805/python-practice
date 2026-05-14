# Reverse Nodes in k-Group for VS Code (Full Program)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):
        
        # Count k nodes
        count = 0
        curr = head
        while curr and count < k:
            curr = curr.next
            count += 1

        # If nodes are less than k
        if count < k:
            return head

        # Reverse first k nodes
        prev = None
        curr = head

        for i in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Recursively reverse next groups
        head.next = self.reverseKGroup(curr, k)

        return prev


# Create Linked List from input
def create_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head

    for num in arr[1:]:
        curr.next = ListNode(num)
        curr = curr.next

    return head


# Print Linked List
def print_linked_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


# Driver Code
nums = list(map(int, input("Enter linked list values: ").split()))
k = int(input("Enter k: "))

head = create_linked_list(nums)

sol = Solution()
new_head = sol.reverseKGroup(head, k)

print("Reversed in k-group:")
print_linked_list(new_head)  