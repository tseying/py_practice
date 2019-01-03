class Solution(object):
    def DecimalToBinary(self, strs):
        num = int(strs)
        list = ""
        if num == 0:
            list += "0"
        while num >= 1:
            Inchar = num % 2
            num = (num - Inchar) / 2
            list += str(Inchar)
        list = list[::-1]
        return list



# =========================================
solution = Solution()
strs = "0"
print solution.DecimalToBinary(strs)
