import sys
from collections import deque
sys.stdin = open("input.txt","r")

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while q:
        sz, sx, sy = q.popleft()
        for i in range(6):
            tx, ty ,tz  = sx + dx[i] , sy + dy[i], sz + dz[i]
            if tx < 0 or tx == n or ty < 0 or ty == m or tz < 0 or tz == h:
                continue
            if arr[tz][tx][ty] == 0:
                arr[tz][tx][ty] = arr[sz][sx][sy] + 1
                q.append([tz, tx, ty])

m,n,h = map(int,input().split())
arr = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

q = deque()
for z in range(h):
    for x in range(n):
        for y in range(m):
            if arr[z][x][y] == 1:
                q.append([z,x,y])

bfs()

flag = False
result = -1
for i in arr:
    for j in i:
        for k in j:
            #만약 배열에 0이 있으면 변경해준다.
            if k == 0:
                flag = True
            #나온 값중 가장 큰 값이 토마토가 전부 익는 날짜
            result = max(result, k)
if flag:
    print(-1)
#전부 익어있으면
elif result == 1:
    print(0)
else:
    print(result - 1)