class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        worfNum = 0
        index = 0
        while index < len(s):
            if s[index] != " ":
                index += 1
                worfNum += 1
            else:
                worfNum = 0
                index += 1
        return worfNum


        # cnt, tail = 0, len(s) - 1
        # while tail >= 0 and s[tail] == ' ':
        #     tail -= 1
        # while tail >= 0 and s[tail] != ' ':
        #     cnt += 1
        #     tail -= 1
        # return cnt

# =========================================
solution = Solution()
s = "a"
print solution.lengthOfLastWord(s)