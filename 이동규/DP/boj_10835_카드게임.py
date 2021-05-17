import sys
sys.stdin = open('input/boj_10835_카드게임.txt', 'r')

N = int(input())
LEFT = list(map(int, input().split()))
RIGHT = list(map(int, input().split()))
memo = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        if LEFT[i] > RIGHT[j]:
            memo[i][j] = max(memo[i][j+1] + RIGHT[j], memo[i+1][j+1], memo[i+1][j])
        else:
            memo[i][j] = max(memo[i + 1][j + 1], memo[i + 1][j])

print(memo[0][0])





