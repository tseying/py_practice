class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        num = 0
        for i in range(len(s) - 1):
            if dic[s[i]] < dic[s[i + 1]]:
                num = num - dic[s[i]]
            else:
                num = num + dic[s[i]]
        num = num + dic[s[-1]]
        return num


# =========================================
solution = Solution()
s = "VVV"
print solution.romanToInt(s)