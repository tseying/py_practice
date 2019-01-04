class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        for i in range(len(nums1)-m):
            nums1.pop()
        nums1 += nums2
        nums1.sort()

        
    #     nums1_index = 0
    #     nums2_index = 0
    #     while (nums1_index < m) and (nums2_index < n):
    #         if nums2[nums2_index] < nums1[nums1_index]:
    #             self.insertWithoutChangingLen(nums1, nums1_index, nums2[nums2_index])
    #             nums2_index += 1
    #             m += 1
    #         else:
    #             nums1_index += 1
    #
    #     if nums2_index != n:
    #         for index in range(nums2_index, n):
    #             self.insertWithoutChangingLen(nums1, nums1_index, nums2[index])
    #             nums1_index += 1
    #
    #     return nums1
    #
    # def insertWithoutChangingLen(self, nums, index, num_to_insert):
    #     length = len(nums)
    #     for i in range(0, length-index-1):
    #         nums[length - 1 - i] = nums[length - 2 - i]
    #
    #     nums[index] = num_to_insert

# =========================================
solution = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print solution.merge(nums1, m, nums2, n)
