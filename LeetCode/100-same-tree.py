#coding=utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:        #相同的二叉树，两边同时有，同时无
            return True
        if p is not None and q is not None:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        else:
            return False

# =========================================
solution = Solution()
p1 = TreeNode(1)
p1.left = None
p1.right = TreeNode(3)
q1 = TreeNode(1)
q1.left = TreeNode(2)
q1.right = TreeNode(3)
print solution.isSameTree(p1, q1)