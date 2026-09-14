txt=input().split(" ")
for i in range(0, len(txt)-1, 2): txt[i+1], txt[i] = txt[i], txt[i+1]
for i in txt: print(i, end=" ")