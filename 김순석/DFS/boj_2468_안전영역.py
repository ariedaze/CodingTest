import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if arr[x][y] <= h:
        return False
    if visit[x][y] == 0:
        visit[x][y] = 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


N = int(input())
arr = []
area = 1

for _ in range(N):
    arr.append(list(map(int, input().split())))

for h in range(1, 101):
    visit = [[0] * (N + 1) for _ in range(N+1)]
    result = 0
    for i in range(N):
        for j in range(N):
            if dfs(i, j) == True:
                result += 1

    if area < result:
        area = result
print(area)