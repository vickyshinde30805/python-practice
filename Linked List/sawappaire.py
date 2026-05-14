# Swap Nodes in Pairs for VS Code (Full Beginner-Friendly Program)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        # If empty or only one node
        if not head or not head.next:
            return head

        new_head = head.next
        prev = None
        curr = head

        while curr and curr.next:
            first = curr
            second = curr.next

            # Swap
            first.next = second.next
            second.next = first

            # Connect previous pair
            if prev:
                prev.next = second

            # Move pointers
            prev = first
            curr = first.next

        return new_head


# Create linked list from array
def create_linked_list(arr):
    if not arr:
        return None

    head = ListNode(arr[0])
    curr = head

    for num in arr[1:]:
        curr.next = ListNode(num)
        curr = curr.next

    return head


# Print linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()


# Driver Code
nums = list(map(int, input("Enter linked list values: ").split()))

head = create_linked_list(nums)

sol = Solution()
new_head = sol.swapPairs(head)

print("After swapping pairs:")
print_linked_list(new_head)