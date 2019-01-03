#coding=utf-8
#典型的斐波拉契数列1，1，2，3，5，8，13
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        times = 1
        num = 0
        i = 1
        while i <= n:
            num , times = times , num + times
            i += 1
        return times

# =========================================
solution = Solution()
n1 = 6
n2 = 5
print solution.climbStairs(n1)
print solution.climbStairs(n2)
