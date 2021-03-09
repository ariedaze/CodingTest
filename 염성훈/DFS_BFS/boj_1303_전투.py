import sys
sys.stdin = open("input.txt","r")

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def calW(x,y):
    global cntW
    visited[x][y] = 1
    for i in range(4):
        tx, ty = x+dx[i], y+dy[i]
        if tx < 0 or tx == M or ty < 0 or ty == N:
            continue
        if arr[tx][ty] == "W" and not visited[tx][ty]:
            visited[tx][ty] = 1
            cntW += 1
            calW(tx,ty)

def calB(x,y):
    global cntB
    visited[x][y] = 1
    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]
        if tx < 0 or tx == M or ty < 0 or ty == N:
            continue
        if arr[tx][ty] == "B" and not visited[tx][ty]:
            visited[tx][ty] = 1
            cntB += 1
            calB(tx, ty)


N, M = map(int,input().split())

arr = [list(map(str,input())) for _ in range(M)]

visited = [[0] * N for _ in range(M)]

cntW = 1
resultW = 0
cntB = 1
resultB = 0

for x in range(M):
    for y in range(N):
        if arr[x][y] == "W" and not visited[x][y]:
            calW(x,y)
            resultW += cntW ** 2
            cntW = 1
        elif arr[x][y] == "B" and not visited[x][y]:
            calB(x,y)
            resultB += cntB ** 2
            cntB = 1

print(resultW, end=" ")
print(resultB)
