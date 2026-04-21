# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root):
        
        def check(node):
            if node is None:
                return 0
            
            left = check(node.left)
            if left == -1:
                return -1
            
            right = check(node.right)
            if right == -1:
                return -1
            
            if abs(left - right) > 1:
                return -1
            
            return max(left, right) + 1
        
        return check(root) != -1


# 🔹 Helper function to build tree manually
def buildTree():
    """
    Example Tree:
            1
           / \
          2   3
         /
        4
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    return root


# 🔹 Main function
if __name__ == "__main__":
    root = buildTree()
    
    sol = Solution()
    result = sol.isBalanced(root)
    
    print("Is Balanced Tree:", result)