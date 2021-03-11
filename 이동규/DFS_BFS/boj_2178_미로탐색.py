import sys
sys.stdin = open('input/boj_2178_미로탐색.txt', 'r')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append([0, 0, 1])

    while queue:
        r, c, d = queue.popleft()
        for i in range(4):
            dr, dc = r + dx[i], c + dy[i]
            if 0 <= dr < ROW and 0 <= dc < COL and matrix[dr][dc] and visit[dr][dc] > d + 1:
                queue.append([dr, dc, d + 1])
                visit[dr][dc] = d + 1

ROW, COL = list(map(int, input().split()))
matrix = [list(map(int, list(input()))) for _ in range(ROW)]
visit = [[99999 for _ in range(COL)] for _ in range(ROW)]
visit[0][0] = 1
result = 9999999

bfs()
print(visit[ROW-1][COL-1])


