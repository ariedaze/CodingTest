import sys
sys.stdin = open('input/boj_11726_2xn 타일링.txt', 'r')

N = int(input())
memo = [0] * 1000
memo[0] = 1
memo[1] = 2

for i in range(2, N):
    memo[i] = memo[i-2] + memo[i-1]

print(memo[N-1] % 10007)