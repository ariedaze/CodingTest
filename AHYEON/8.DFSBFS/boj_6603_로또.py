def johab(begin_with, level):
    if level == 6:
        print(*result)
        return
    for i in range(begin_with, k):
        result[level] = s[i]
        johab(i+1, level+1)


while True:
    i = input()
    if i == '0': break
    i = list(map(int, i.split()))
    k = i[0]
    result = [0]*6
    s = i[1:]
    answer = []
    johab(0, 0)
    print()
