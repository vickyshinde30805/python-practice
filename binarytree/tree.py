class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def createBinaryTree(self, descriptions):
        nodes = {}
        children = set()

        for parent, child, isLeft in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)

            if isLeft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]

            children.add(child)

        for val in nodes:
            if val not in children:
                return nodes[val]


# Test
descriptions = [
    [20, 15, 1],
    [20, 17, 0],
    [15, 10, 1]
]

root = Solution().createBinaryTree(descriptions)

print(root.val)        # 20
print(root.left.val)   # 15
print(root.right.val)  # 17