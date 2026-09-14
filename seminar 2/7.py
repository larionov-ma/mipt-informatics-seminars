line = input().split(" ")
col_max = 0
for i in range(len(line)):
    col = 0
    for j in range(len(line)):
        if line[i] == line[j]:
            col+=1
    if col> col_max:
        col_max = col

for i in range(len(line)):
    col = 0
    for j in range(len(line)):
        if line[i] == line[j]:
            col+=1
    if col == col_max:
        print(line[i])
        break