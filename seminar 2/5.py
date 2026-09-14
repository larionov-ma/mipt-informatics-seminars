txt = input().split(" ")
for i in [txt[-1]]+txt[:-1]: print(i, end=" ")
