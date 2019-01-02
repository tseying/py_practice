class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i <= (len(nums) - 1):
            if nums[i] != val:
                i = i + 1
            else:
                del nums[i]
        return nums


# =========================================
solution = Solution()
nums1 = [3,2,2,3]
val1 = 3
nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
print solution.removeElement(nums1, val1)
print solution.removeElement(nums2, val2)