arr = [1, 5, 2, 4, 5, 6, 7]
i=0
len=len(arr)
def iterr(arr,i,len):
    if i==len:
        return
    print(arr[i])
    i+=1
    iterr(arr,i,len)


iterr(arr,i,len)