class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list = []
        for index in range(len(nums)):
            for i in range((index + 1), len(nums)):
                if nums[index] + nums[i] == target:
                    list.append(index)
                    list.append(i)
                    break
            if list != []:
                break
        return list




# =========================================
solution = Solution()
nums = [11, 2, 15, 7, 1, 8]
target = 9
print solution.twoSum(nums, target)