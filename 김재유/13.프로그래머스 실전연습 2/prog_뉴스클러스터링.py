str1 = "aa1+aa2"
str2 = "AAAA12"

str1 = [str1[i:i+2] for i in range(len(str1)-1)]
str2 = [str2[i:i+2] for i in range(len(str2)-1)]
list_str1 = {}
list_str2 = {}
chars = []
child = 0
parent = 0
for string in str1:
    if string.isalpha():
        if string.lower() in list_str1.keys():
            list_str1[string.lower()] += 1
        else:
            list_str1[string.lower()] = 1
        if string.lower() not in chars:
            chars.append(string.lower())
for string in str2:
    if string.isalpha():
        if string.lower() in list_str2.keys():
            list_str2[string.lower()] += 1
        else:
            list_str2[string.lower()] = 1
        if string.lower() not in chars:
            chars.append(string.lower())

for char in chars:
    if char in list_str1.keys() and char in list_str2.keys():
        child += min(list_str1[char], list_str2[char])
        parent += max(list_str1[char], list_str2[char])
    elif char in list_str1.keys():
        parent += list_str1[char]
    else:
        parent += list_str2[char]

if parent:
    result = int(child/parent*65536)
else:
    result = 65536
print(result)
