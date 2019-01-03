class Solution(object):
    def BinaryToDecimal(self, strs):
        num = 0
        reverse_strs = strs[::-1]
        for i in range(len(reverse_strs)):
            num += int(reverse_strs[i]) * (2 ** i)
        return num

# =========================================
solution = Solution()
strs = "0"
print solution.BinaryToDecimal(strs)