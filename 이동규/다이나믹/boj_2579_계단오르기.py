import sys
sys.stdin = open('input/boj_2579_계단오르기.txt', 'r')

# DP를 이용한 풀이
N = int(input())
stairs = [int(input()) for _ in range(N)]
memo = [0] * N

if N >= 1:
    memo[0] = stairs[0]
if N >= 2:
    memo[1] = stairs[0] + stairs[1]
if N >= 3:
    memo[2] = max(memo[0] + stairs[2], stairs[1] + stairs[2])
if N > 3:
    for i in range(3, N):
        memo[i] = max(memo[i-3]+stairs[i-1], memo[i-2]) + stairs[i]

print(memo[N-1])

# # 재귀를 사용한 DPS 백트레킹은 시간초과 ㅠ
# def dynamic_duo(now_stair, prev, sum_score):
#     global MAX;
#     if now_stair == N-1:
#         if sum_score > MAX:
#             MAX = sum_score
#         return
#
#     if prev == 1:
#         dynamic_duo(now_stair + 1, -1, sum_score + DP_stairs[now_stair+1])
#     elif prev == -1:
#         pass
#     else:
#         dynamic_duo(now_stair + 1, 1, sum_score + DP_stairs[now_stair + 1])
#
#     if now_stair + 2 <= N-1:
#         dynamic_duo(now_stair + 2, 1, sum_score + DP_stairs[now_stair+2])
#
#
#
# DP_stairs = []
# N = int(input())
# MAX = 0
#
# for i in range(N):
#     DP_stairs.append(int(input()))
#
# dynamic_duo(-1, 0, 0)
#
# print(MAX)



