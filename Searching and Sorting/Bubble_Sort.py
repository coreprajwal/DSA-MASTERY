##Buble Sort

arr=[5,8,9,3,1,2]

for i in range(0,len(arr)):

    for j in range(i+1,len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j],arr[j+1]

print(arr)