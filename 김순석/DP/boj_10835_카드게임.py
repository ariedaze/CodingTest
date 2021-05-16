# 버리는 경우 : 왼 / 왼+오 / 오
# 왼 > 오 : 무조건 오른쪽 버린다
# 왼 <= 오 : 왼쪽 / 왼 + 오 버릴때마다 비교에서 dp에 저장
# 왼쪽을 버려 오른쪽 값보다 큰게 나올 때 까지 / 같이 버려서 다음 값 비교


import sys
ln = sys.stdin.readline

N = int(ln())
left = list(map(int, ln().split()))
right = list(map(int, ln().split()))
dp = [[0] * (N + 1) for _ in range(N + 1)]

max_a = max(left)
max_b = max(right)
cnt = 0

if max_a > max_b:
    cnt = sum(right)
    print(cnt)
    exit()

for i in range(N -1, -1, -1):
    for j in range(N - 1, -1, -1):
        if left[i] > right[j]:
            # 오른쪽 버린거, 둘다 버린거, 왼쪽 버린거
            dp[i][j] = max(dp[i][j + 1] + right[j], dp[i + 1][j + 1], dp[i + 1][j])
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1])

print(dp[0][0])