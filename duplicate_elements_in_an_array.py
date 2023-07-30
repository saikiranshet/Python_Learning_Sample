arr = [1,1,2,3,4,5,6,6,7,7,7,9,2,9]
n = len(arr)
a1 = []
for num in arr:
    if num not in a1:
        a1.append(num)
print(a1)