import sys
sys.stdin = open('boj_11066.txt', 'r')
from sys import stdin

readline = stdin.readline

for _ in range(int(input())):
    N = int(input())
    nums = list(map(int, readline().split()))

    dp = [[0] * N for _ in range(N)]

    sums = [0] * (N + 1)
    for n in range(1, N + 1):
        sums[n] = sums[n - 1] + nums[n - 1]

    for gap in range(1, N + 1):
        for i in range(N - gap):
            j = i + gap
            dp[i][j] = 0xffffffffff
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + sums[j + 1] - sums[i])

    print(dp[0][N - 1])