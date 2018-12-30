arry = ['hello', 'world', 'me', 'and', 'you']
dic = {}

for index in range(len(arry)):
    key = arry[index]
    dic[key] = index

for key in dic:
    print key, ':', dic[key]