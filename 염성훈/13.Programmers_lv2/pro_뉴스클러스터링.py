def solution(str1, str2):
    s1 = []
    for i in range(len(str1) - 1):
        if str1[i:i+2].isalpha():
            s1.append(str1[i:i+2].lower())

    s2 = []
    for i in range(len(str2) - 1):
        if str2[i:i + 2].isalpha():
            s2.append(str2[i:i + 2].lower())

    union = sum(max(s1.count(i), s2.count(i)) for i in set(s1) | set(s2))
    intersec = sum(min(s1.count(i), s2.count(i)) for i in set(s1) & set(s2))

    if union == 0: return 65536

    return int((intersec / union) * 65536)

str1 = 'aa1+aa2'
str2 = 'AAAA12'
print(solution(str1,str2))