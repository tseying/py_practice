# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            return self.digui(root.left, root.right)
        else:
            return True

    def digui(self, q, p):
        if q and p:
            if q.val == p.val and self.digui(q.left, p.right) and self.digui(q.right, p.left):
                return True
            else:
                return False
        if not q and not p:
            return True
        else:
            return False

# =========================================
solution = Solution()
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)
print solution.isSymmetric(root1)
