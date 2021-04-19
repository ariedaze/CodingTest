import sys
sys.stdin = open('input/boj_12026_BOJ 거리.txt', 'r')

CHAR = ['B', 'O', 'J']
N = int(input())
L = list(input())
memo = [999999999] * N
memo[0] = 0

for i in range(N):
    for j in range(i+1, N):
        if memo[i] != 999999999 and L[j] == CHAR[(CHAR.index(L[i]) + 1) % 3] and memo[j] > memo[i] + (j-i) ** 2:
            memo[j] = memo[i] + (j-i) ** 2

print(-1 if memo[-1] == 999999999 else memo[-1])
