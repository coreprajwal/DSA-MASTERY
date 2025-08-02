##Buble Sort

arr=[5,8,9,3,1,2]


def bubblesort(arr):
    for i in range(0,len(arr)):
        endd=len(arr)-i-1
        for j in range(0,endd):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

print(bubblesort(arr))