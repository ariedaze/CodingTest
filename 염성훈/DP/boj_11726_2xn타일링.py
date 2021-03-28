import sys
sys.stdin = open("input.txt","r")


n = int(input())

dp = []
dp.append(1)
dp.append(2)

if n == 1:
    print(dp[0])
elif n == 2:
    print(dp[1])
else:
    for i in range(2,n):
        dp.append(dp[i-2]+dp[i-1])

    print(dp[-1] % 10007)
