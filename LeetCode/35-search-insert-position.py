class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= nums[0]:
            return 0
        if target > nums[len(nums) - 1]:
            return len(nums)
        for i in range(len(nums) - 1):
            if nums[i] < target and target <= nums[i + 1]:
                return i + 1


# =========================================
solution = Solution()
nums1= [1,3,5,6]
target1 = 5
nums2 = [1,3,5,6]
target2 = 2
nums3 = [1,3,5,6]
target3 = 7
nums4 = [1,3,5,6]
target4 = 0
print solution.searchInsert(nums1, target1)
print solution.searchInsert(nums2, target2)
print solution.searchInsert(nums3, target3)
print solution.searchInsert(nums4, target4)
