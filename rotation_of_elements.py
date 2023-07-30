def rotateNumber(lists,num):
    output_List = []
    for item in range(len(lists)-num,len(lists)):
        output_List.append(item)
    for item in range(0,len(lists)-num):
        output_List.append(item)
    return output_List

lists = [1,2,3,4,5,6,7,8,9]
num = 5
print(rotateNumber(lists,num))