class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        if len(strs) > 0:
            shortestWord = self.getShortestWord(strs)
            for index in range(len(shortestWord)):
                if self.sameIndexHasSameChar(strs, index):
                    result = result + shortestWord[index]
                else:
                    break

            return result



    def sameIndexHasSameChar(self, strs, index):
        compare = strs[0]
        for s in strs:
            if s[index] != compare[index]:
                return False
        return True


    def getShortestWord(self, strs):
        if len(strs) > 0:
            minLength = len(strs[0])
            shortestWord = strs[0]
            for s in strs:
                if len(s) < minLength:
                    minLength = len(s)
                    shortestWord = s
            return s





# =========================================
solution = Solution()
strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]
print solution.longestCommonPrefix(strs1)
print solution.longestCommonPrefix(strs2)