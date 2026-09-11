txt = input().upper()
arr=[]
CH=[['E','3'],['J','L'],['S','2'],['Z','5'],['3','E'],['L','G'],['2','S'],['5','Z']]
for i in range(len(txt)):
    arr.append(txt[i])


def rotate(arr):
    result = []
    for i in range(len(arr)-1, -1, -1):
        result.append(arr[i])
    return result





def change_ch(arr):
    for i in range(len(arr)):
        for j in range(len(CH)):
            if arr[i] == CH[j][0]:
                arr[i] = CH[j][1]
    return arr[i]

ARR1 = [
    'A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8',
    '0',
]
ARR2 = [
    'E', 'J', 'S', 'Z',
    '3', 'L', '2', '5'
]
ARR3=[
    '4', '6', '7', '9',
    'B','C','D','F','G','K','N','P','Q','R'
]




change_ch(arr)

