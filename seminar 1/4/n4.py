f = open("input.txt", 'r')

a = f.readlines()
arr = []
for i in a:
    i = i.split('\n')[0]
    i = i.split(' ')
    arr = arr + i


nums = arr[:-1]
op = arr[-1]




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
        

f = open("output.txt", 'w')
f.write(str(r))
f.close()




