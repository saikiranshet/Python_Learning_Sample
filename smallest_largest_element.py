arr = [10,20,12,11,22,33,1,1,2,3,3,0]
min = arr[0]
max = arr[0]
for i in range(len(arr)):
    if arr[i]<min:
        min = arr[i]
    
    if arr[i]>max:
        max = arr[i]
print("MAX ELEMENTS",max)
print("MIN ELEMENTS",min)