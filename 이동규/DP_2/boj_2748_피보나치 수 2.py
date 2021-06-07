import sys
sys.stdin = open('input/boj_2748_피보나치 수 2.txt', 'r')

N = int(input())
before_previous = 0
previous = 1

for i in range(0, N-2):
    temp = previous
    previous = previous + before_previous
    before_previous = temp


print(previous + before_previous)

# # DP 정석풀이
# n = int(input())
# dp = [0 for _ in range(91)]
# dp[0] = 0
# dp[1] = 1
# for i in range(2, n+1):
#     dp[i] = dp[i-1] + dp[i-2]
# print(dp[n])