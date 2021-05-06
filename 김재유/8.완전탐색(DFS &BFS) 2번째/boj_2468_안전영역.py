import sys; sys.stdin = open('input_data/2468.txt')
sys.setrecursionlimit(100000)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(x,y):
    visit[x][y] = 1
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < size and 0 <= ty < size and ground[tx][ty] > 0 and not visit[tx][ty]:
            DFS(tx, ty)

size = int(input())
ground = [list(map(int, input().split())) for _ in range(size)]
count = 1
result = []
while count:
    count = 0
    visit = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if not visit[i][j] and ground[i][j] > 0:
                DFS(i,j)
                count += 1
    for i in range(size):
        for j in range(size):
            ground[i][j] -= 1
    result.append(count)
print(max(result))
