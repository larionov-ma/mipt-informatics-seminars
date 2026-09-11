
N = int(input())
b = int(input())
c = int(input())

n10 = int(f"{N}", b)

arr = []

if n10!=0:
    

    while n10 !=0:
        arr = [n10%c] + arr
        n10 = n10 // c
    result = ""
    for i in arr:
        result += str(i)
    print(result)
else:
    print(0)




