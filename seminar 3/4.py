n, l = input().split(' ')
n = int(n)
arr = []

if n%2!=0:
    for i in range(1, n//2 + 2):
        arr.append(l*i)
    for i in range(n//2, 0, -1):
        arr.append(l*i)

if n %2 == 0:
    for i in range(1, n//2+1):
        arr.append(l*i)
    for i in range(n//2, 0, -1):
        arr.append(l*i)



for i in arr:
    print(i)