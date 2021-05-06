import sys
sys.stdin = open("input.txt","r")

n = int(input())

def dfs(x,y):
    global home
    visited[x][y] = 1

    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]
        if tx < 0 or tx == n or ty < 0 or ty == n:
            continue
        if arr[tx][ty] == 1 and not visited[tx][ty]:
            visited[tx][ty] = 1
            home += 1
            dfs(tx,ty)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = [list(map(int,input())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
total = 0
result = []
for x in range(n):
    for y in range(n):
        if arr[x][y] and not visited[x][y]:
            home = 1
            total += 1
            dfs(x,y)
            result.append(home)
            home = 1

print(total)
result.sort()
for item in result:
    print(item)
