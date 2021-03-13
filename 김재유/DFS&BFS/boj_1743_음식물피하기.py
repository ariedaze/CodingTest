import sys;
sys.stdin = open('input_data/1743.txt')
sys.setrecursionlimit(1000000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(x, y):
    global max_depth
    global depth
    check[x][y] = 1
    depth += 1
    if depth > max_depth:
        max_depth = depth
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < height and 0 <= ty < width and not check[tx][ty] and ground[tx][ty]:
            DFS(tx, ty)

height, width, trash = map(int, input().split())
ground = [[0]*width for _ in range(height)]
check = [[0]*width for _ in range(height)]
for _ in range(trash):
    x, y = map(int, input().split())
    ground[x-1][y-1] = 1

max_depth = 0
for x in range(height):
    for y in range(width):
        if not ground[x][y] or check[x][y]: continue
        depth = 0
        DFS(x, y)
print(max_depth)
