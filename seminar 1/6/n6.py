f = open("input.txt", 'r')

a = f.readlines()
arr = []
for i in a:
    i = i.split('\n')[0]
    i = i.split(' ')
    arr = arr + i

nums = arr[:-2]
op = arr[-2]
osn = int(arr[-1])
nums = [int(i, osn)for i in nums]

if op == "+":
    r = 0
    for i in nums:
        r = r + int(i)
elif op == '*':
    r = 1
    for i in nums:
        r = r * int(i)
elif op == '-':
    r = int(nums[0])
    for i in range(1, len(nums)):
        r = r - int(nums[i])
 
arr = []

if r!=0:
    

    while r !=0:
        arr = [r%osn] + arr
        r = r // osn
    result = ""
    for i in arr:
        result += str(i)
else:
    result = 0


f = open("output.txt", 'w')
f.write(str(result))
f.close()






