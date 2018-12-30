class Solution():
    def replaceAllSpaceWithDot(self, sentence):
        dic = {}
        word_list = sentence.split(' ')
        result_sentence = ','.join(word_list)
        return result_sentence

# ====================================
solution = Solution()
sentence1 = "my name is jack and jack is my best friend jack is good"
sentence2 = "mike and jack meet nancy nancy meets mike and jack"
print solution.replaceAllSpaceWithDot(sentence1)
print solution.replaceAllSpaceWithDot(sentence2)