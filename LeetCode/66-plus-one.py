class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strs = ""
        list = []
        for i in range(len(digits)):
            strs += str(digits[i])
        num = int(strs)
        num += 1
        strs = str(num)
        for index in range(len(strs)):
            list.append(int(strs[index]))
        return list


# =========================================
solution = Solution()
digits1 = [9,9]
digits2 = [4,3,2,1]
print solution.plusOne(digits1)
print solution.plusOne(digits2)