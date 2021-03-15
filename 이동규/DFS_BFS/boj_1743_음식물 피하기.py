import sys
sys.stdin = open('input/boj_1743_음식물 피하기.txt', 'r')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(index):
    r, c = index
    queue = deque()
    queue.append(index)
    visit[r][c] = True
    size = 0

    while queue:
        r, c = queue.popleft()
        size += 1
        for i in range(4):
            dr, dc = r + dx[i], c + dy[i]
            if 0 <= dr < ROW and 0 <= dc < COL and matrix[dr][dc] and visit[dr][dc] == False:
                queue.append([dr, dc])
                visit[dr][dc] = True

    return size

ROW, COL, NUM = list(map(int, input().split()))
matrix = [[0 for _ in range(COL)] for _ in range(ROW)]
visit = [[False for _ in range(COL)] for _ in range(ROW)]
result = 0

for _ in range(NUM):
    r, c = list(map(int, input().split()))
    matrix[r-1][c-1] = 1

for r in range(ROW):
    for c in range(COL):
        if visit[r][c] == False and matrix[r][c]:
            temp = bfs([r, c])
            if temp > result:
                result = temp

print(result)


