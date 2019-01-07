#coding=utf-8
#死循环
list = [1,2,3]
while list:
    list.append(4)
print list
