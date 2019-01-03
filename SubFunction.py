class Solution(object):
    def main(self, a, b, c, d):
        x = self.getMax(a, b)
        y = self.getMax(c, d)
        z = self.getMax(x, y)
        print z


    def getMax(self, x, y):
        if x > y:
            return x
        else:
            return y




# =========================================
solution = Solution()
a = 1
b = 2
c = 3
d = 4
solution.main(a,b,c,d)