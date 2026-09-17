ARR = ['.', '?', '!']
with open('input.txt', 'r') as f:
    lines = f.readlines()
    count = 0
    for i in lines:
        remove_double = False
        for j in i:
            if j in ARR:
                if not remove_double:
                    count +=1
                    remove_double = True
            else:
                remove_double = False

    print(count)
