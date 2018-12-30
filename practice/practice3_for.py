class Solution():
    def getWordCountDict(self, sentence):
        dic = {}
        word_list = sentence.split(' ')
        for word in word_list:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1

        return dic

# ====================================
solution = Solution()
sentence1 = "my name is jack and jack is my best friend jack is good"
sentence2 = "mike and jack meet nancy nancy meets mike and jack"
print solution.getWordCountDict(sentence1)
print solution.getWordCountDict(sentence2)