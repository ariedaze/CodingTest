import sys; sys.stdin = open('input_data/2234.txt')
from collections import deque
# 좌 상 우 하
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def DFS(x, y):
    global count
    count +=1
    visit[x][y] = region
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if not Ground[x][y] & (1<<i) and not visit[tx][ty]:
            DFS(tx, ty)

width, height = map(int, sys.stdin.readline().split())
Ground = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
visit = [[0]*width for _ in range(height)]
results = []
region = 0
for i in range(height):
    for j in range(width):
        if not visit[i][j]:
            count = 0
            region += 1
            DFS(i, j)
            results.append(count)

result_3 = 0
for x in range(height):
    for y in range(width):
        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < height and 0 <= ty < width and visit[x][y] != visit[tx][ty]:
                if result_3 < results[visit[x][y]-1] + results[visit[tx][ty]-1]:
                    result_3 = results[visit[x][y]-1] + results[visit[tx][ty]-1]
print(len(results))
print(max(results))
print(result_3)