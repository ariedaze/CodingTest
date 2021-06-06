dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

M, N, K = map(int, input().split())
arr = [[0] * N for _ in range(M)]

count = 0
result = []

for k in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            arr[i][j] = 1


def dfs(x, y):
    global area, count
    area = 1
    S = []
    S.append([x, y])
    arr[x][y] = 1

    while S:
        x, y = S.pop()

        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if tx <= -1 or tx >= M or ty <= -1 or ty >= N:
                continue

            if arr[tx][ty] == 0:
                arr[tx][ty] = 1
                area += 1
                S.append([tx, ty])
    return area


for i in range(M):
    for j in range(N):
        if arr[i][j] == 0:
            dfs(i, j)
            result.append(area)

result.sort()
print(len(result))
for i in result:
    print(i, end=' ')