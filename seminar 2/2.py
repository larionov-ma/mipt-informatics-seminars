n, t = input().split(' ')
n = int(n)
l = len(t)
arr =[]
c = int(l/n)
for i in range(c):
    arr += [t[i*c:i*c+c]]

def get_mirror(arr):
    mirror = []
    for i in range(len(arr)-1, -1, -1):
            mirror.append(arr[i])
    return mirror
        
def array_to_str(arr):
    result = ''
    for i in arr:
        result += i
    return result

print(arr)

for i in range(len(arr)):
    txt = arr[i]
    txt = [j for j in txt]
    arr[i]=txt



for i in range(len(arr)):
     arr[i] = get_mirror(arr[i])


for i in range(len(arr)):
     arr[i] = array_to_str(arr[i])

print(array_to_str(arr))

