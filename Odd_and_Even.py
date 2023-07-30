
def oddEven(arr):
    even = []
    odd = []
    for i in arr:
        if i % 2==0:
            even.append(i)
        else:
            odd.append(i)
    print(even)
    print(odd)

arr = [1,2,3,4,5,6,7,8,9,10,11,12]
oddEven(arr)
