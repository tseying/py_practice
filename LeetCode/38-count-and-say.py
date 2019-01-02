class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        if n == 1:
            result = "1"
            return result
        strs = self.countAndSay(n - 1)
        count = 0
        pre = strs[0]
        for index in range(len(strs)):
            now = strs[index]
            if now == pre:
                count = count + 1
            else:
                result = result + str(count) + str(pre)
                count = 1
                pre = now

        result = result + str(count) + str(pre)
        return result


# =========================================
solution = Solution()
n1 = 1
n2 = 4
print solution.countAndSay(n1)
print solution.countAndSay(n2)