import sys; sys.stdin = open('input_data/2583.txt')
sys.setrecursionlimit(10000000)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(x, y):
    global depth
    global result
    visit[x][y] = 1
    depth += 1
    if depth > result:
        result = depth

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < height and 0 <= ty < width and not visit[tx][ty] and not Ground[tx][ty]:
            DFS(tx, ty)


width, height, N = map(int, input().split())
Ground = [[0] * width for _ in range(height)]
visit = [[0] * width for _ in range(height)]
results = []
for _ in range(N):
    x_start, y_start, x_end, y_end = map(int, input().split())
    for x in range(x_start, x_end):
        for y in range(y_start, y_end):
            Ground[x][y] = 1


for i in range(height):
    for j in range(width):
        if not Ground[i][j] and not visit[i][j]:
            result = 0
            depth = 0
            DFS(i,j)
            results.append(result)
results.sort()
print(len(results))
print(*results)
