import sys
sys.stdin = open("input.txt","r")

input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)
days = []

for i in range(n):
    days.append(tuple(map(int,input().split())))

for i in range(n-1, -1, -1):
    if days[i][0] + i > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i+1],dp[i+days[i][0]]+days[i][1])


print(max(dp))