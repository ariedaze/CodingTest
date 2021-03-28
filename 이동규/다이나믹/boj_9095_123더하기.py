import sys
sys.stdin = open('input/boj_9095_123더하기.txt', 'r')

# DP
DP = [-1] * 11
DP[0] = 0
DP[1] = 1
DP[2] = 2
DP[3] = 4

def dynamic_duo(num):
    if DP[num] != -1:
        return DP[num]

    for i in range(4, num+1):
        DP[i] = DP[i-1] + DP[i-2] + DP[i-3]

    return DP[num]


for T in range(int(input())):
    N = int(input())

    print(dynamic_duo(N))



# DFS로 백트래킹하여 푸는 법
# def dfs(num, depth):
#     global result
#
#     if num == N:
#         result += 1
#         return
#
#     if num + 1 <= N:
#         dfs(num+1, depth+1)
#
#
#     if num + 2 <= N:
#         dfs(num+2, depth+1)
#
#     if num + 3 <= N:
#         dfs(num+3, depth+1)
#
#
# for T in range(int(input())):
#     N = int(input())
#
#     result = 0
#
#     dfs(0, 0)
#     print(result)