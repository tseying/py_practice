# encoding=utf-8
s = "abcdefgababejdsxcdaswcdfeewfsadscdfffsdsadsaczccaasdwscxzcsadwdaswqdsa"
count_dic = {}
for c in s:
    if c in count_dic:
        count_dic[c] = count_dic[c] + 1     # 也可以使用"自加"符号+=，执行效率更高: count_dic[c] += 1，同理还有-=，*=，/=
    else:                                   # 如果字典中没有key，则需要将key加入，同时将value置为1
        count_dic[c] = 1

for key in count_dic:
    print key, ":", count_dic[key]
