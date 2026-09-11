arr = input().split(" ")
n = len(arr)
s = 1
for i in arr:
    s *= int(i)
print(s**(1/n))
