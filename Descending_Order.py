arr = [1,11,22,0,2,3,46,177,19]
n = len(arr)
for i in range(n):
    min = i
    for j in range(i+1,n):
        if arr[j]>arr[min]:
            min = j
    temp =  arr[i]
    arr[i] = arr[min]
    arr[min] = temp
print(arr)