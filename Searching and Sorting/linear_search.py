#Linear Search

arr=[2,4,6,9,1,5,8]
num=9

def linsearch(arr,num):
    for i in range(0,len(arr)):
        if arr[i]==num:
            return i
        elif i==len(arr)-1:
            return -1

result=linsearch(arr,num)
if result==-1:
    print("No element mathched with the number:",result)
else:
    print(arr[result],"found at index",result)

