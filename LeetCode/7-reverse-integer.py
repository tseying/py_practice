class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if x >= 0:
            y = s[: : -1]
        else:
            z = s[1 :]
            y = '-' + z[: : -1]

        y = float(y)
        if (y <= float(-2 ** 31)) or (y >= float(2 **31 - 1)):
            return 0
        else:
            return int(y)

# =========================================
solution = Solution()
x1 = 2**31 - 1
x2 = -123
x3 = 120
print solution.reverse(x1)
print solution.reverse(x2)
print solution.reverse(x3)