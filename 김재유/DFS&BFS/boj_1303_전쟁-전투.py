import sys; sys.stdin = open('input_data/1303.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(x, y, color):
    global max_depth
    global depth
    check[x][y] = 1
    depth += 1
    if depth > max_depth:
        max_depth = depth
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < height and 0 <= ty < width and not check[tx][ty] and ground[tx][ty] == color:
            DFS(tx, ty, color)

width, height = map(int, input().split())

ground = [list(' '.join(input().split())) for _ in range(height)]
check = [[0]*width for _ in range(height)]
W, B = 0, 0
for x in range(height):
    for y in range(width):
        if check[x][y]: continue
        max_depth = 0
        depth = 0
        color = ground[x][y]
        DFS(x, y, color)
        if color == 'W':
            W += max_depth**2
        else:
            B += max_depth**2
print(W, B)



