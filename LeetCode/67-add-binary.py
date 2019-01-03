#coding=utf-8
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1 = self.BinaryToDecimal(a)
        num2 = self.BinaryToDecimal(b)
        summation = num2 + num1
        strs = self.DecimalToBinary(str(summation))
        return strs

    def BinaryToDecimal(self,strs):
        num = 0
        reverse_strs = strs[::-1]
        for i in range(len(reverse_strs)):
            num += int(reverse_strs[i]) * (2 ** i)
        return num                    #返回数字

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
        return list                   #返回字符串


# =========================================
solution = Solution()
a1 = "0"
b1 = "0"
a2 = "1010"
b2 = "1011"
print solution.addBinary(a1, b1)
print solution.addBinary(a2, b2)