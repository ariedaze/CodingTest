import sys
sys.stdin = open('input/boj_2156_포도주 시식.txt', 'r')

N = int(input())
WINES = [int(input()) for _ in range(N)]
memo = [[0, 0] for _ in range(N)]



if N == 1:
    memo[0][0], memo[0][1] = 0, WINES[0]
    print(memo[0][1])
elif N == 2:
    memo[1][0], memo[1][1] = WINES[0], WINES[0] + WINES[1]
    print(memo[1][1])
else:
    memo[0][0], memo[0][1] = 0, WINES[0]
    memo[1][0], memo[1][1] = WINES[0], WINES[0] + WINES[1]
    for i in range(2, N):
        memo[i][0] = max(memo[i-1][1], memo[i-1][0])
        memo[i][1] = max(memo[i-1][0] + WINES[i], memo[i-2][0] + WINES[i-1] + WINES[i])

    print(max(memo[N-1][0], memo[N-1][1]))