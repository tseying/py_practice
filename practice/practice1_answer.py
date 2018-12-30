class Solution():
    def findSecondCharAInList(self, list):
        '''
        return the index of the second 'A' in the list,
        if there is not two 'A' in the list, return -1
        :param list:
        :return: index(int)
        '''
        countA = 0
        for index in range(len(list)):
            if list[index] == 'A':
                countA += 1
            if countA == 2:
                return index

        return -1




# ===================================== under this line are tests
solution = Solution()
s1 = ['B', 'A', 'A']
s2 = ['A', 'C', 'D', 'A']
s3 = ['A', 'B', 'D']
print solution.findSecondCharAInList(s1)
print solution.findSecondCharAInList(s2)
print solution.findSecondCharAInList(s3)