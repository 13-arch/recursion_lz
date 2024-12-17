def partitions(a):
    if a==0:
        return a
    return 1+partitions(a-1)
num=partitions(4)
print(num)