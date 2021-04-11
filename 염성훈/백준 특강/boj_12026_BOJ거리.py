import sys
sys.stdin = open("input.txt","r")

n = int(input())
lst = input()

MAX = 999999999
# dp[i] 가 의미하는 것은 i까지 오는데 드는 최소 에너지의 양을 나타낸다.
dp = [MAX] * n

# 현재 올 수 있는 이전의 알파벳을 찾는다.
def get_prev(x):
    if x == "B":
        return "J"
    elif x == "O":
        return "B"
    elif x == "J":
        return "O"

dp[0] = 0
for i in range(1, n):
    prev = get_prev(lst[i])
    for j in range(i):
        #BOJ순서대로 오는지 확인하기위해 현재 값의 이전 값이랑 같으면 i(현재위치)와 j(이전위치)에서
        #dp[i]의 값 = 현재위치까지오는데 드는 최소 에너지의양, dp[j](이전 위치까지 오는데 오는 최소 에너지의양)
        #에 현재위치까지 이동했을때의 에너지를 더해준 값중 최소값을 비교해서 현재 위치의 에너지에 넣는다.
        #민약 O다음에 J값이 없으면 B의 이전 값은 J이기 떄문에
        if lst[j] == prev:
            dp[i] = min(dp[i], dp[j] + pow(i - j, 2))

print(dp[n - 1] if dp[n - 1] != MAX else -1)