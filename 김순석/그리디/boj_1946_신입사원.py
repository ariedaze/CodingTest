import sys
In = sys.stdin.readline
T = int(In())
for t in range(1, T+1):
    N = int(In())
    score = []
    cnt = 1
    for _ in range(N):
        score.append(list(map(int, In().split())))

    score = sorted(score, key=lambda x: x[0])
    pivot = score[0][1]
    if score[0][0] == 1 and score[0][1] == 1:
        print(1)
        continue

    for i in range(1, N):
        if pivot > score[i][1]:
            cnt += 1
            pivot = score[i][1]

    print(cnt)
