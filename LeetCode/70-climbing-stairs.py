class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        times = 1
        if n <= 1:
            return times
        if n >= 2:
            times1 = self.climbStairs(n - 1)
            times2 = self.climbStairs(n - 2)
            times = times1 + times2
        return times



# =========================================
solution = Solution()
n1 = 6
n2 = 5
print solution.climbStairs(n1)
print solution.climbStairs(n2)