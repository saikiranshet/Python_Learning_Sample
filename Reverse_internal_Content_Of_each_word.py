str1 = "SAIKIRAN SHET IS A HERO"
str2 = str1.split(" ")
str3 = []
for i in str2:
    str3.append(i[::-1])
str4 = " ".join(str3)
print(str4)