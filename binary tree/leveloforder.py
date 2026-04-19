from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        q = deque([root])
        ans = []

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            ans.append(level)

        return ans


# ----------- Helper Function to Build Tree -----------
def build_tree(values):
    """
    Build tree from level order list
    Example: [1,2,3,None,4]
    """
    if not values:
        return None

    root = TreeNode(values[0])
    q = deque([root])
    i = 1

    while q and i < len(values):
        node = q.popleft()

        if values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1

    return root


# ----------- MAIN FUNCTION -----------
if __name__ == "__main__":
    # Input (level order)
    values = [1, 2, 3, 4, 5, None, 6]

    root = build_tree(values)

    sol = Solution()
    result = sol.levelOrder(root)

    print("Level Order Traversal:")
    print(result)