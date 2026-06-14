class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# Create linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

slow = fast = head

while fast and fast.next:
    print(f"Before: slow={slow.val}, fast={fast.val}")

    slow = slow.next
    fast = fast.next.next

    if fast:
        print(f"After : slow={slow.val}, fast={fast.val}")
    else:
        print(f"After : slow={slow.val}, fast=None")

print("\nMiddle (start of second half) =", slow.val)