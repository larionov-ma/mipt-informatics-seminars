txt = input().upper()
arr=[]
CH=[['E','3'],['J','L'],['S','2'],['Z','5'],['3','E'],['L','J'],['2','S'],['5','Z']]

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

answers = [
    	[0, " is not a palindrome."],
        [1, " is a regular palindrome."],
        [2, " is a mirrored string."],
        [3, " is a mirrored palindrome."]

]


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
    return arr

def have_ch(arr, ARR):
    for i in arr:
        if i in ARR:
            return True
    return False



def remove_answer(index):
    for i in range(len(answers)):
        if answers[i][0] == index:
            answers.pop(i)
            return




if have_ch(arr, ARR2) or have_ch(arr, ARR3):
    remove_answer(3)

if rotate(arr) != arr:
    remove_answer(1)
    remove_answer(3)


#пернеделать
if  not have_ch(arr, ARR2):
    remove_answer(2)





