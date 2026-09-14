line = input().split(" ")
for i in range(len(line)):
    flag = True
    for j in range(len(line)):
        if line[i] == line[j] and i!=j:
            flag = False
            break

    if flag:
        print(line[i], end=" ")