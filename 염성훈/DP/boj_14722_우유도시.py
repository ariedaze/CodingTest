import sys
sys.stdin = open("input.txt","r")
sys.setrecursionlimit(100000)

dx = [1, 0]
dy = [0, 1]

def dfs(x,y):
    for i in range(2):
        tx, ty = x+dx[i], y + dy[i]
        if tx >= N or ty >= N:
            continue
        if arr[tx][ty] == dp[x][y] % 3 and not visited[tx][ty]:
            visited[tx][ty] = 1
            dp[tx][ty] = dp[x][y] + 1
            dfs(tx,ty)
        elif arr[tx][ty] != dp[x][y] % 3 and not visited[tx][ty]:
            dp[tx][ty] = dp[x][y]
            dfs(tx,ty)

N = int(input())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dp[0][0] = 1
visited[0][0] = 1
dfs(0, 0)

print(dp[N-1][N-1])
print(dp)