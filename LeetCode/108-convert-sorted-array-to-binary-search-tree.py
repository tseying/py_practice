#coding=utf-8
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            root = TreeNode(None)
            return root
        if len(nums) == 1:
            root = TreeNode(nums[0])
            return root
        if len(nums) > 1:
            midIndex = (len(nums) - 1) / 2
            root = TreeNode(nums[midIndex])
            nums1 = nums[0 : midIndex]                      #前闭后开啊大姐！！！
            nums2 = nums[midIndex + 1 : len(nums)]
            root.left = self.sortedArrayToBST(nums1)
            root.right = self.sortedArrayToBST(nums2)
            return root

# =========================================
solution = Solution()
nums = [-10, -3, 0, 5, 9]
print solution.sortedArrayToBST(nums)