ARR = ['.', '?', '!']
ARR2 = ['MR', 'MRS', 'DR']
with open('input.txt', 'r') as f:
    lines = f.readlines()
    count = 0
    for i in lines:
        remove_double = False
        for j in i:
            if j in ARR:
                if not remove_double:
                    count +=1
                    remove_double = True
            else:
                remove_double = False

    count2 = 0
    for i in lines:
        line = i.split(" ")
        line = [j for j in line if j !="" and j!='\n']
        dot_end = [j for j in line if j[-1]=='.']
        initials = [j for j in dot_end if len(j) == 2]
        sokrashenia = [j for j in dot_end if (j[:-1].upper() in ARR2)]
        count2 += len(initials) + len(sokrashenia)


    
    print(count - count2)
