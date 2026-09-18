n = int(input())
line = input().split()
m = len(line)//2

i = 0
while i < len(line):
    k = 0
    k_up = -1
    j = 0
    while j < len(line):
        if int(line[i])>int(line[j]):
            k += 1
            k_up+=1
        elif int(line[i])==int(line[j]):
            k_up += 1
        j+=1
    if m >= k and m <= k_up:
        print(line[i])
        break
    i+=1






