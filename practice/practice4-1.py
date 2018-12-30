class Solution(object):
    def string2int(self, string):
        '''
        :param string:
        :return: int
        '''
        i = intern(string)
        print i

    def int2string(self, int):
        '''

        :param int:
        :return: string
        '''
        s = str(int)
        print s


# ========================================================
solution = Solution()
string1 = "123bb"
string2 = "281"
print solution.string2int(string1)
print solution.string2int(string2)
