n, t = input().split(' ')
n = int(n)
l = len(t)
arr =[]
c = int(l/n)
for i in range(c):
    arr += [t[i*c:i*c+c]]


print(arr)
for i in range(len(arr)):
    txt = arr[i]
    txt = [j for j in txt]
    arr[i]=txt

print(arr)
mirror_arr = []
