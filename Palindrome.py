str1 = input("Enter the string:\n")
var = ""
for i in str1:
    var = i + var
if var == str1:
    print("PALINDROME")
else:
    print("NOT PALINDROME")