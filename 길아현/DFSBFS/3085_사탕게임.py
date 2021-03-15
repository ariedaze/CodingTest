def cnt():
    global N, ans
    for i in range(N):
        c = 1
        for j in range(1, N):
            if candies[i][j] == candies[i][j-1]:
                c += 1
            else:
                ans = max(ans, c)
                c = 1
        if ans < c: ans = c

    for i in range(N):
        c = 1
        for j in range(1, N):
            if candies[j][i] == candies[j-1][i]:
                c += 1
            else:
                ans = max(ans, c)
                c = 1
        if ans < c: ans = c


N = int(input())
candies = [list(input()) for _ in range(N)]

ans = 0

for i in range(N):
    for j in range(1, N):
        candies[i][j], candies[i][j-1] = candies[i][j-1], candies[i][j]
        cnt()
        candies[i][j], candies[i][j-1] = candies[i][j-1], candies[i][j]

        candies[j][i], candies[j-1][i] = candies[j-1][i], candies[j][i]
        cnt()
        candies[j][i], candies[j - 1][i] = candies[j-1][i], candies[j][i]

print(ans)