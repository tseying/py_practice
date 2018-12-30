m = int(input())
n = int(input())

list = []

for i in range(len(list)):
    list[0] = m + n
    list[1] = m * n
    list[2] = m ** n
    list[3] = m % n
    if m < n:
        list[4] = n
    else:
        list[4] = m
    print list
    