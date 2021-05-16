import sys
ln = sys.stdin.readline

dx = [0, 1]
dy = [1, 0]

N = int(ln())
lst = [list(map(int, ln().split())) for _ in range(N)]
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]


if lst[0][0] == 0:
    dp[0][0][0] = 1
# i-1 이나 j-1처럼 이 전의 값을 비교할려고 초기값 설정했음.
for i in range(1, N):
    flag = lst[0][i]
    if flag == 0:
        dp[0][i][0] = dp[0][i-1][2] + 1
    else:
        dp[0][i][0] = dp[0][i-1][0]

    if flag == 1 and dp[0][i][2] < dp[0][i][0]:
        dp[0][i][1] = dp[0][i-1][0] + 1
    else:
        dp[0][i][1] = dp[0][i-1][1]

    if flag == 2 and dp[0][i][0] < dp[0][i][1]:
        dp[0][i][2] = dp[0][i-1][1] + 1
    else:
        dp[0][i][2] = dp[0][i-1][2]


for i in range(1, N):
    flag = lst[i][0]
    if flag == 0:
        dp[i][0][0] = dp[i-1][0][2] + 1
    else:
        dp[i][0][0] = dp[i-1][0][0]

    if flag == 1 and dp[i][0][2] < dp[i][0][0]:
        dp[i][0][1] = dp[i-1][0][0] + 1
    else:
        dp[i][0][1] = dp[i-1][0][1]

    if flag == 2 and dp[i][0][0] < dp[i][0][1]:
        dp[i][0][2] = dp[i-1][0][1] + 1
    else:
        dp[i][0][2] = dp[i-1][0][2]


# (1, 1)부터 시작
for i in range(1, N):
    for j in range(1, N):
        flag = lst[i][j]

        if flag == 0:
            dp[i][j][0] = max(dp[i-1][j][2] + 1, dp[i][j-1][2] + 1)
        else:
            dp[i][j][0] = max(dp[i-1][j][0], dp[i][j-1][0])

        if flag == 1 and dp[i][j][2] < dp[i][j][0]:
            dp[i][j][1] = max(dp[i-1][j][0] + 1, dp[i][j-1][0] + 1)
        else:
            dp[i][j][1] = max(dp[i-1][j][1], dp[i][j-1][1])

        if flag == 2 and dp[i][j][0] < dp[i][j][1]:
            dp[i][j][2] = max(dp[i-1][j][1] + 1, dp[i][j-1][1] + 1)
        else:
            dp[i][j][2] = max(dp[i][j-1][2], dp[i-1][j][2])

# for i in dp:
#     print(*i)
print(max(max(dp[i][j] for i in range(N) for j in range(N))))