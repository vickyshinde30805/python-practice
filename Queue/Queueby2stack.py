class Stack:
    def __init__(self):
        self.val = []

    def push(self, x):
        self.val.append(x)

    def pop(self):
        if len(self.val) == 0:
            return -1
        return self.val.pop()

    def top(self):
        if len(self.val) == 0:
            return -1
        return self.val[-1]

    def size(self):
        return len(self.val)


class MyQueue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x):
        while self.s1.size() > 0:
            self.s2.push(self.s1.pop())

        self.s1.push(x)

        while self.s2.size() > 0:
            self.s1.push(self.s2.pop())

    def pop(self):
        return self.s1.pop()

    def peek(self):
        return self.s1.top()

    def empty(self):
        return self.s1.size() == 0


# ✅ Driver Code (for VS Code)
if __name__ == "__main__":
    q = MyQueue()

    print("Push elements: 10, 20, 30")
    q.push(10)
    q.push(20)
    q.push(30)

    print("Peek:", q.peek())   # 10
    print("Pop:", q.pop())     # 10
    print("Peek:", q.peek())   # 20
    print("Is Empty:", q.empty())  # False

    print("Pop:", q.pop())     # 20
    print("Pop:", q.pop())     # 30
    print("Is Empty:", q.empty())  # True