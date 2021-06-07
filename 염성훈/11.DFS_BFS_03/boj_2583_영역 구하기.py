import sys
sys.stdin = open("input.txt","r")
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    q = deque()
    q.append([x,y])
    arr[x][y] = 1
    answer = 1
    while q:
        rx,ry = q.popleft()
        for i in range(4):
            tx, ty = rx + dx[i], ry + dy[i]
            if tx < 0 or tx == m or ty < 0 or ty == n:
                continue
            if not arr[tx][ty]:
                arr[tx][ty] = 1
                answer += 1
                q.append([tx,ty])

    return answer

m, n, k = map(int,input().split()) #m이 x축의 길이 n은 y축의 길이, k개의 직사각형 영역

arr = [[0] * n for _ in range(m)]

for _ in range(k):
    sx, sy, ex, ey = map(int,input().split())

    #이게 좀 어려웠음 주어진 영역을 -1로 채우고
    for i in range(sy,ey):
        for j in range(sx,ex):
            arr[i][j] = -1

result = []

for x in range(m):
    for y in range(n):
        if not arr[x][y]:
            result.append(bfs(x,y))

result.sort()
print(len(result))
print(*result)






