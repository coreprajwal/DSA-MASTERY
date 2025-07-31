## Last Occurence using recursion

arr=[1,2,5,7,2,9,5,8]
num=5
lenn=len(arr)
def occur(arr,lenn,num):
    if arr[lenn]==num:
        return lenn
    elif lenn==0:
        return -1
    lenn-=1
    return occur(arr,lenn,num)


print(occur(arr,lenn-1,num))