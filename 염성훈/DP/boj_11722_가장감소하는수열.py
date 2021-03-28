import sys
sys.stdin = open("input.txt","r")

n = int(input())
lst = list(map(int, input().split()))

dp = [1 for i in range(n)]

#이해가안가서 구글링해본 문제.
for i in range(n):
    for j in range(i):
        if lst[i] < lst[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))