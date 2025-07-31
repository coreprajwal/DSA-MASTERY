## Binary Search

arr=[2,4,6,89,1,8]
arr.sort()
print(arr)
num=1000
L=0
R=len(arr)-1
def binarysearchh(arr,num,L,R):
    while L<=R:
        mid=(L+R)//2
        value=arr[mid]
        if value==num:
            break

        elif value>num:
            R=mid-1

        else:
            L=mid+1
    else:
        mid=-1
    return mid


result=binarysearchh(arr,num,L,R)
if result==-1:
    print("Element doesn't exist in the array:",result)
else:
    print(f"Element {num} exist at position:",result)