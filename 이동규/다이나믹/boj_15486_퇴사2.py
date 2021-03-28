sys.stdin = open('input/boj_15486_퇴사2.txt', 'r')

import sys
input = sys.stdin.readline

N = int(input())
TP = [list(map(int, input().split())) for _ in range(N)]
memo = [0] * 1500001

for i in range(N-1, -1, -1):
    if TP[i][0] + i > N: # 시간 기한을 지킬 수 없는 일이라면
        memo[i] = memo[i+1]
    else:
        memo[i] = max(memo[i+1], TP[i][1]+memo[i+TP[i][0]])

print(memo[0])