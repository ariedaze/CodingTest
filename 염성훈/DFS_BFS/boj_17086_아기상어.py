import sys
sys.stdin = open("input.txt","r")
from collections import deque

def bfs():
    while Q:
        cx,cy = Q.popleft()
        for i in range(8):
            tx, ty = cx + dx[i], cy + dy[i]
            if tx < 0 or tx == N or ty < 0 or ty == M:
                continue
            if not arr[tx][ty]:
                Q.append([tx,ty])
                arr[tx][ty] = arr[cx][cy] + 1
    return



N, M = map(int,input().split()) #N이 세로 M이 가로

arr = [list(map(int,input().split())) for _ in range(N)]

# 상하좌우대각선
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

Q = deque()

for x in range(N):
    for y in range(M):
        if arr[x][y] == 1:
            Q.append([x,y])

bfs()
max_value = 0

for r in range(N):
    for c in range(M):
        if arr[r][c] > max_value:
            max_value = arr[r][c]

print(max_value - 1)



