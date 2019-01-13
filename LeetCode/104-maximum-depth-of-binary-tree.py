# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root is not None:
            leftDeepth = self.maxDepth(root.left)
            rightDeepth = self.maxDepth(root.right)
            return max(leftDeepth,rightDeepth) + 1


# =========================================
solution = Solution()
root = TreeNode(3)
root.right = TreeNode(5)
root.left = TreeNode(9)
root.right.right = TreeNode(4)
root.right.left = TreeNode(2)
print solution.maxDepth(root)