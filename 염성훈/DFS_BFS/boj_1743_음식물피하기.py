import sys
sys.setrecursionlimit(100000) #안해주면 런타임에러남 dfs사용해서 재귀호출이 너무 많이 됬을떄 사용한다. \
sys.stdin = open("input.txt","r")

def dfs(x,y):
    global temp
    visited[x][y] = 1

    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]
        if tx < 0 or tx == N or ty < 0 or ty == M:
            continue
        if arr[tx][ty] and not visited[tx][ty]:
            visited[tx][ty] = 1
            temp += 1
            dfs(tx,ty)


N, M, K = map(int,input().split()) #N은 세로길이 M은 가로길이

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

temp = 1
ans = 0

for _ in range(K):
    x, y = map(int,input().split())
    arr[x-1][y-1] = 1

for r in range(N):
    for c in range(M):
        if arr[r][c] == 1:
            dfs(r,c)
            if ans < temp:
                ans = temp
            temp = 1

print(ans)




