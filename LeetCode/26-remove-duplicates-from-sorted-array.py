class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while (i + 1) <= (len(nums)-1):
            if nums[i] != nums[i + 1]:
                i = i + 1
            else:
                del nums[i + 1]
                i = i



# =========================================
solution = Solution()
nums1 = [1,1,2]
nums2 = [0,0,1,1,1,1,2,3,3,4,4,5,5]
print solution.removeDuplicates(nums1)
print solution.removeDuplicates(nums2)