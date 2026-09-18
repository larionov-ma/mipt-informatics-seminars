line = input().split(" ")
col_max = 0


i = 0
while i < len(line):
    col = 0
    j = 0
    while j < len(line):
        if line[i] == line[j]:
            col+=1
        j+=1
    if col> col_max:
        col_max = col
    i+=1


i = 0
while i < len(line):
    col = 0
    j = 0
    while j < len(line):
        if line[i]==line[j]:
            col+=1
        j += 1
    if col == col_max:
        print(line[i])
        break
    i+=1


