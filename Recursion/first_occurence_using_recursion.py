
#Find first occurence of a number in array using recursion


arr = [1, 5, 2, 4, 5, 6, 7]
num=5
i=0
def occur(arr,i,num):
    if arr[i]==num:
        return i
    i+=1
    return occur(arr,i,num)


print(occur(arr,i,num))