n = int(input())
store = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if store[i][j] == 0:
            dp[i][j] = 1

for i in range(n):
    for j in range(n):
        count = dp[i][j]
        next1 = (i+1, j)
        next2 = (i, j+1)

        if next1[0] < n:
            if store[next1[0]][next1[1]] == count % 3:
                dp[next1[0]][next1[1]] = max(count + 1, dp[next1[0]][next1[1]])
            else:
                dp[next1[0]][next1[1]] = max(count, dp[next1[0]][next1[1]])

        if next2[1] < n:
            if store[next2[0]][next2[1]] == count % 3:
                dp[next2[0]][next2[1]] = max(count + 1, dp[next2[0]][next2[1]])
            else:
                dp[next2[0]][next2[1]] = max(count, dp[next2[0]][next2[1]])


print(dp[n-1][n-1])

