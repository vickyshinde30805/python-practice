class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head):

        if head is None or head.next is None:
            return None

        # Count nodes
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next

        # Find middle index
        k = n // 2

        # Go to node before middle
        curr = head
        for _ in range(k - 1):
            curr = curr.next

        # Delete middle node
        curr.next = curr.next.next

        return head


# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Call function
sol = Solution()
head = sol.deleteMiddle(head)

# Print linked list
curr = head
while curr:
    print(curr.val, end=" -> " if curr.next else "")
    curr = curr.next