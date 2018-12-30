class Solution():
    def findSecondCharAInList(self, list):
        '''
        return the index of the second 'A' in the list,
        if there is not two 'A' in the list, return -1
        :param list:
        :return: index(int)
        '''
        dict = {}

        for element in list:
            if element in dict:
                dict[element] = dict[element] + 1
            else:
                dict[element] = 1

        if dict['A'] < 2:
            return -1





# ===================================== under this line are tests
solution = Solution()
s1 = ['B', 'A', 'A']
s2 = ['A', 'C', 'D', 'A']
s3 = ['A', 'B', 'D']
print solution.findSecondCharAInList(s1)
print solution.findSecondCharAInList(s2)
print solution.findSecondCharAInList(s3)