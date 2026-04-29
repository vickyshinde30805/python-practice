# Definition for binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p, q):
        
        # If both nodes are empty
        if not p and not q:
            return True
        
        # If one is empty or values differ
        if not p or not q or p.val != q.val:
            return False
        
        # Check left and right subtree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Helper function to build tree from list
def build_tree(values):
    if not values or values[0] is None:
        return None

    nodes = []

    # Create nodes
    for val in values:
        if val is not None:
            nodes.append(TreeNode(val))
        else:
            nodes.append(None)

    child_index = 1

    # Connect children
    for i in range(len(values)):
        if nodes[i] is not None:
            if child_index < len(values):
                nodes[i].left = nodes[child_index]
                child_index += 1

            if child_index < len(values):
                nodes[i].right = nodes[child_index]
                child_index += 1

    return nodes[0]


# Input first tree
tree1 = input("Enter first tree values (use None for empty): ").split()

# Input second tree
tree2 = input("Enter second tree values (use None for empty): ").split()

# Convert input
tree1 = [None if x == "None" else int(x) for x in tree1]
tree2 = [None if x == "None" else int(x) for x in tree2]

# Build trees
p = build_tree(tree1)
q = build_tree(tree2)

# Check trees
solution = Solution()

if solution.isSameTree(p, q):
    print("Both trees are same")
else:
    print("Trees are different")