import sys
sys.stdin = open("input.txt","r")

N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

## 1,2개만 있을경우 그냥 그 값이 된다.
dp = [0 for _ in range(N)]
dp[0] = arr[0]
if N == 1:
    print(dp[0])
else:
    dp[1] = arr[0] + arr[1]
    # dp의 다음 값을 넣어 정해준다.
    for i in range(2, N):
        dp[i] = max(dp[i-1], dp[i-2] + arr[i], dp[i-3] + arr[i] + arr[i-1])

    print(dp[N-1])