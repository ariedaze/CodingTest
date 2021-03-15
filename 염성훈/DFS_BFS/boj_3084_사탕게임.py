import sys
sys.stdin = open("input.txt","r")
from collections import deque

def check_arr():
    global cnt
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            Q = deque([])
            Q.append([r, c])
            check_x = -1
            check_y = -1
            if not visited[r][c]:
                visited[r][c] = 1
                while Q:
                    sx, sy = Q.popleft()
                    if sx == check_x:
                        for i in range(2,4):
                            nx, ny = sx + dx[i], sy + dy[i]
                            if nx < 0 or nx == N or ny < 0 or ny == N:
                                continue
                            if not visited[nx][ny] and arr[sx][sy] == arr[nx][ny]:
                                visited[nx][ny] = visited[sx][sy] + 1
                                Q.append([nx, ny])
                                if visited[nx][ny] > cnt:
                                    cnt = visited[nx][ny]
                    elif sy == check_y:
                        for i in range(2):
                            nx, ny = sx + dx[i], sy + dy[i]
                            if nx < 0 or nx == N or ny < 0 or ny == N:
                                continue
                            if not visited[nx][ny] and arr[sx][sy] == arr[nx][ny]:
                                visited[nx][ny] = visited[sx][sy] + 1
                                Q.append([nx, ny])
                                if visited[nx][ny] > cnt:
                                    cnt = visited[nx][ny]
                    else :
                        for i in range(4):
                            nx, ny = sx + dx[i], sy + dy[i]
                            if nx < 0 or nx == N or ny < 0 or ny == N:
                                continue
                            if not visited[nx][ny] and arr[sx][sy] == arr[nx][ny]:
                                visited[nx][ny] = visited[sx][sy] + 1
                                Q.append([nx,ny])
                                check_x = nx
                                check_y = ny
                                if visited[nx][ny] > cnt:
                                    cnt = visited[nx][ny]


N = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = [list(input()) for _ in range(N)]
cnt = 0

for x in range(N):
    for y in range(N):

        for i in range(4):
            tx, ty = x+dx[i], y+dy[i]

            if tx < 0 or tx == N or ty < 0 or ty == N:
                continue

            if arr[x][y] != arr[tx][ty]:
                temp = arr[x][y]
                arr[x][y] = arr[tx][ty]
                arr[tx][ty] = temp
                check_arr()
                arr[tx][ty] = arr[x][y]
                arr[x][y] = temp

print(cnt)
