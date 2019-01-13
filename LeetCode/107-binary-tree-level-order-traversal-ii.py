#coding=utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        List = []
        if root is None:
            return List
        stack = [root]
        while len(stack) != 0:
            temporary = []                      #temporary是用来提供索引，将stack的内容换为：i.left & i.right（都是指针类型，不是整数型！！！）
            eachResult = []
            for i in stack:
                eachResult.append(i.val)
                if i.left is not None:
                    temporary.append(i.left)
                if i.right is not None:
                    temporary.append(i.right)
            stack = temporary
            List.insert(0, eachResult)           #这里不能用append->因为append是在末尾加入，而用insert就可以从第一位插入->按照正常的情况遍历
        return List

# =========================================
solution = Solution()
root = TreeNode(3)
root.right = TreeNode(9)
root.left = TreeNode(20)
root.right.left = TreeNode(7)
root.right.right = TreeNode(5)
print solution.levelOrderBottom(root)