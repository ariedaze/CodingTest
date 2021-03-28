import sys
sys.stdin = open("input.txt","r")
sys.setrecursionlimit(100000)

def dfs(x,y):
    global cnt

    if x == 0 and y == 0:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if tx < 0 or tx == M or ty < 0 or ty == N:
                continue
            if arr[x][y] < arr[tx][ty]:
                dp[x][y] += dfs(tx,ty)
    return dp[x][y]

M, N = map(int,input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]

dp = [[-1]* N for _ in range(M)]

print(dfs(M - 1, N - 1))



