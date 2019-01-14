# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if root is not None:
            deepth = abs(self.maxDeepth(root.right) - self.maxDeepth(root.left))
            if deepth > 1:
                return False
            else:
                if self.isBalanced(root.right) and self.isBalanced(root.left):
                    return True
                else:
                    return False

    def maxDeepth(self,root):
        if not root:
            return 0
        else:
            leftDeepth = self.maxDeepth(root.left)
            rightDeepth = self.maxDeepth(root.right)
            return max(leftDeepth,rightDeepth) + 1

# =========================================
solution = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = TreeNode(3)
print solution.isBalanced(root)