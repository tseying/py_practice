#coding=utf-8
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            if i + len(needle) < len(haystack):          #注意循环的顺序，先哪一层，再到哪一层；i从0开始，没有这个条件，则直接判断0就开始return
                if haystack[i : (i + len(needle))] == needle:
                    return i
            else:
                if haystack[i : (i + len(needle))] == needle:
                    return i
                else:
                    return -1


# =========================================
solution = Solution()
haystack1 = "hello"
needle1 = "ll"
haystack2 = "aaaaa"
needle2 = "bba"
print solution.strStr(haystack1, needle1)
print solution.strStr(haystack2, needle2)