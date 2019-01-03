class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        sqrt_num = x ** 0.5
        return int(sqrt_num)

# =========================================
solution = Solution()
x1 = 4
x2 = 8
print solution.mySqrt(x1)
print solution.mySqrt(x2)