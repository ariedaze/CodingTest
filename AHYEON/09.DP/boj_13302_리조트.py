n, m = map(int, input().split())
vacation = [0] * (106)

if m:
    for mi in map(int, input().split()):
        vacation[mi] = 1

dp = [[987654321]*(106) for _ in range(106)]
dp[0][0] = 0

for i in range(n+1):
    for j in range(i+1):
        if dp[i][j] == 987654321: continue

        now = dp[i][j]

        if vacation[i+1]:
            dp[i+1][j] = min(now, dp[i+1][j])

        if j >= 3:
            dp[i+1][j-3] = min(dp[i+1][j-3], now)

        dp[i+1][j] = min(now + 10000, dp[i + 1][j])

        for k in range(1, 4):
            dp[i + k][j + 1] = min(now + 25000, dp[i + k][j + 1])

        for k in range(1, 6):
            dp[i + k][j + 2] = min(now + 37000, dp[i + k][j + 2])

ans = 987654321

for i in range(n):
    ans = min(ans, dp[n][i])

print(ans)
