class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        y = s[: : -1]

        if y == s:
            return True
        else:
            return False

# =========================================
solution = Solution()
x1 = 121
x2 = -121
x3 = 11111111111111
print solution.isPalindrome(x1)
print solution.isPalindrome(x2)
print solution.isPalindrome(x3)