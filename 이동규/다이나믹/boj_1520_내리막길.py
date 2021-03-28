import sys
sys.stdin = open('input/boj_1520_내리막길.txt', 'r')
from collections import deque

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append([0, 0])

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            dr, dc = r + dy[i], c + dx[i]
            if 0 <= dr < ROW and 0 <= dc < COL and M[dr][dc] < M[r][c]:
                if dr == ROW-1 and dc == COL - 1:
                    visit[dr][dc] += 1
                    continue
                queue.append([dr, dc])
                visit[dr][dc] += 1
    return visit[ROW-1][COL-1]

ROW, COL = list(map(int, input().split()))
M = [list(map(int, input().split())) for i in range(ROW)]
visit = [[0 for _ in range(COL)] for _ in range(COL)]

print(bfs())