m = int(input())
n = int(input())

list = []

list.append(str(m + n))
list.append(str(m * n))
list.append(str(m ** n))
list.append(str(m % n))
if m > n:
    list.append(str(m))
else:
    list.append(str(n))
print list