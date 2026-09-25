a, b = input().split(" ")
a, b = int(a), int(b)
answer = []

def get_nod(a, b, ost=min(a, b)):
    arr = sorted([a, b])
    new_ost = arr[1]%arr[0]
    if new_ost == 0:
        return ost
    return get_nod(arr[0], new_ost, new_ost)

d = get_nod(a, b)


s = -1
flag = True
while flag:
    s+=1
    x = -s
    y = s - abs(x)
    arr = [[x, y]]
    x+=1
    while x <= s:
        y = s - abs(x)
        arr.append([x, y])
        arr.append([x, -y])
        x+=1
    new_arr = []
    for i in arr:
        if not (i in new_arr):
            new_arr.append(i)
    new_arr = sorted(new_arr)

    for i in new_arr:
        if a * i[0] + b*i[1] == d:
            print(i[0], i[1], d)
            flag = False
            break