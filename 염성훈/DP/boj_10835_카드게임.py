import sys
sys.stdin = open("input.txt","r")
n = int(input())
left = list(map(int,input().split()))
right = list(map(int,input().split()))

# 여기서 dp[i][j]는 왼쪽카드 에서 i장, 오른쪽 더미카드에서 j장 버렸을때의 최댓값을 나타낸다.
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n -1, -1, -1):
    for j in range(n -1, -1, -1):
        # 오른쪽이 왼쪽보다 더 작다면 1)오른쪽 아래값과 현재 오른쪽의 값, 2)왼쪽 아래값, 3) 오른쪽, 왼쪽 아랫값의 최댓값을 비교해서 다음 최댓값 선정
        if right[j] < left[i]:
            dp[i][j] = max(dp[i][j + 1] + right[j], dp[i + 1][j], dp[i + 1][j + 1])
        # 오른쪽이 더 크면 왼쪽 아래를 제거했을때 최대값과 둘다 제거했을때 값 중 최댓값이 들어간다.
        else:
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1])

print(dp[0][0])