a = input().split(' ')
n = int(a[0])
a = a[1:]
a = [int(i) for i in a]

for i in range(1, n+1):
    if not (i in a):
        print(i)
        break
