import sys
In = sys.stdin.readline
T = int(In())
for t in range(1, T+1):
    N = int(In())
    score = []
    cal = []
    result = []
    for _ in range(N):
        score.append(list(map(int, In().split())))

    a = sorted(score, key=lambda x: x[0])
    if a[0][0] == 1 and a[0][1] == 1:
        print(1)
        continue

    for i in range(1, len(a)):
        if a[0][1] > a[i][1]:
            cal.append(a[i])

    cal = sorted(cal, key=lambda x: x[1])
    for i in range(1, len(cal)):
        if cal[0][0] > cal[i][0]:
            result.append(cal[i])
    print(len(result) + 2)
