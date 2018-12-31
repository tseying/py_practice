#coding=nutf-8
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        minLength = len(strs[0])
        minLengthWord = strs[0]
        for s in strs:
            if len(s) < minLength:
                minLength = len(s)
                minLengthWord = s

        commonPrefix = ""
        shouldEnd = False
        for index in range(minLength):
            commonChar = minLengthWord[index]
            for s in strs:
                if s[index] != minLengthWord[index]:
                    shouldEnd = True
                    break
            if shouldEnd:                                  #为了跳出最外面的循环#
                break
            commonPrefix = commonPrefix + commonChar

        return commonPrefix

# =========================================
solution = Solution()
strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]
print solution.longestCommonPrefix(strs1)
print solution.longestCommonPrefix(strs2)