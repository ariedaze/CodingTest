import sys
sys.stdin = open("input.txt","r")
from collections import deque

def bfs():
    q = deque()
    q.append([r1,c1])
    arr[r1][c1] = 1
    while q:
        x, y  = q.popleft()
        for i in range(6):
            tx, ty = x + dx[i], y + dy[i]
            if tx < 0 or tx >= n or ty < 0 or ty >= n:
                continue
            if not arr[tx][ty]:
                arr[tx][ty] = arr[x][y] + 1
                q.append([tx,ty])

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

n = int(input())
r1, c1, r2, c2 = map(int,input().split())
arr = [[0] * n for _ in range(n)]

bfs()

print(arr[r2][c2] - 1)