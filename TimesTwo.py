s = "kshidhoihednjshcauoh"
list = {}

for key in s:
    if key in list:
        list[key] = list[key] + 1
    else:
        list[key] =1

for key in list:
    print key, ':', list[key]



