class Solution():
    def get_the_appearing_most_char_number(self, sentence):
        '''
        find the appearing-most char in a english sentence,
        for example:
        "helloworld"
        you should return 3

        tips:
        use list.sort()
        or use max()
        :param sentence:
        :return: int
        '''
        list = []
        dict = {}

        for element in sentence:
            if element in dict:
                dict[element] = dict[element] + 1
                list.append(dict[element])
            else:
                dict[element] = 1
                list.append(dict[element])

        result = []
        most_appearing_num = max(list)
        for key in dict:
            if dict[key] == most_appearing_num:
                result.append(key)

        return result




# ====================================
solution = Solution()
sentence1 = "helloworldo"
sentence2 = "youshouldgohome"
sentence3 = "atleastyoualsohaveme"
print solution.get_the_appearing_most_char_number(sentence1)
print solution.get_the_appearing_most_char_number(sentence2)
print solution.get_the_appearing_most_char_number(sentence3)