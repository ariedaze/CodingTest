import sys
import copy
sys.setrecursionlimit(1000000)
sys.stdin = open("input.txt","r")

def dfs(x,y):
    visited[x][y] = 1
    for i in range(4):
        tx, ty = x + dx[i], y + dy[i]
        if tx < 0 or tx == n or ty < 0 or ty == n:
            continue
        if not visited[tx][ty] and temp[tx][ty]:
            visited[tx][ty] = 1
            dfs(tx,ty)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())

arr = [list(map(int,input().split())) for _ in range(n)]

max_value = 0
result = []

for x in range(n):
    for y in range(n):
        if arr[x][y] > max_value:
            max_value = arr[x][y]

while max_value:
    temp = copy.deepcopy(arr)
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for r in range(n):
        for c in range(n):
            if temp[r][c] < max_value:
                temp[r][c] = 0

    for k in range(n):
        for z in range(n):
            if not visited[k][z] and temp[k][z]:
                cnt += 1
                dfs(k,z)
    result.append(cnt)
    max_value -= 1

print(max(result))