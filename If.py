# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
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
q = TreeNode(1)
q.right = TreeNode(2)
q.left = TreeNode(2)
p = TreeNode(1)
p.left = TreeNode(1)
p.right = TreeNode(2)
print solution.digui(q, p)