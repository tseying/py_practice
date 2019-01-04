class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        getMaxSum = nums[0]
        i = 0
        summation = 0
        while i >= 0 and i <= (len(nums) - 1):
            if summation >= 0:
                summation += nums[i]
                if summation >= getMaxSum:
                    getMaxSum = summation
            else:
                summation = nums[i]
            if summation >= getMaxSum:
                getMaxSum = summation
            i += 1
        return getMaxSum


# =========================================
solution = Solution()
nums = [-2,1,3,4,-1,2,1,-5,4]
print solution.maxSubArray(nums)
