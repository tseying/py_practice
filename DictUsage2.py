englishi_dict = {
    'one' : 1,
    'two' : 2,
    'three' : 3
}
chinese_dict = {}

for key in englishi_dict:
    i = englishi_dict[key],
    chinese_dict[i] = key

for i in chinese_dict:
    print i, ':', chinese_dict[i]