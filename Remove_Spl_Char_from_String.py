import re

str1 = "SAIKIRAN**&&!!SHET@20^"
pattern = r'[^a-zA-Z0-9]'
str2 = re.sub(pattern,"",str1)
print(str2)