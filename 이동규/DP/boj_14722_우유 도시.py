import sys
sys.stdin = open('input/boj_14722_우유 도시.txt', 'r')
from collections import deque


def dfs():
    stack = deque()
    stack.append([0, 0, 1])

    while stack:
        r, c, target = stack.pop()
        for dx, dy in [(1, 0), (0, 1)]:
            for i in range(1, N):
                dr, dc = r + (dx*i), c + (dy*i)
                if 0 <= dr < N and 0 <= dc < N and MILK_STORE[dr][dc] == target and memo[dr][dc] + 1 > memo[r][c]:
                    stack.append([dr, dc, (target + 1) % 3])
                    memo[dr][dc] = memo[r][c] + 1
                    break


N = int(input())
MILK_STORE = [list(map(int, input().split())) for i in range(N)]
memo = [[0 for _ in range(N)] for _ in range(N)]
if MILK_STORE[0][0] != 0:
    print(1)
else:
    dfs()
    print(max(max(memo))+1)