##Selection Sort
arr=[9,2,4,9,1,3,22]

for i in range(0,len(arr)):
    min_idx=i
    for j in range(i+1,len(arr)):
       if arr[min_idx]>arr[j]:
           min_idx=j
    arr[i],arr[min_idx]=arr[min_idx],arr[i]

print(arr)