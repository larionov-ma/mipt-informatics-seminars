n = int(input())
line = input().split()
m = n//2 + 1

for i in range(len(line)):
    k = 0
    for j in range(len(line)):
        if line[i]>=line[j]:
            k += 1
    if k == m:
        print(line[i])
        break

