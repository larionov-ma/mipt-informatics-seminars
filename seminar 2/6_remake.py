arr = input().split(" ")
i = 0
while i < len(arr):
    flag = True
    j = 0
    while j < len(arr):
        if i !=j and arr[i]==arr[j]:
            flag = False
            break
        j += 1
    if flag:
        print(arr[i], end=' ')
    i += 1
