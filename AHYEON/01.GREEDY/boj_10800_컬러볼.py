import sys
input = sys.stdin.readline


N = int(input())

ball = [[0, 0, i] for i in range(N)]
ans = [0 for i in range(N)]

for i in range(N):
    ball[i][1], ball[i][0] = map(int, input().split())

ball.sort()

colors = [0 for i in range(N + 1)]
s = 0
j = 0

for i in range(N):
    while ball[j][0] < ball[i][0]:
        colors[ball[j][1]] += ball[j][0]
        s += ball[j][0]
        j += 1

    ans[ball[i][2]] = s - colors[ball[i][1]]

for i in range(N):
    print(ans[i])
