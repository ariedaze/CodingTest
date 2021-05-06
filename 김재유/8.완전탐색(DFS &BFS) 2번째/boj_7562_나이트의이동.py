import sys; sys.stdin = open('input_data/7562.txt')
from collections import deque

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]


for t in range(int(input())):
    size = int(input())
    visit = [[1000]* size for _ in range(size)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    Q = deque()
    Q.append([start_x, start_y])
    visit[start_x][start_y] = 0
    while Q:
        x, y = Q.popleft()
        for i in range(8):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx < size and 0 <= ty < size:
                if visit[tx][ty] > visit[x][y] + 1:
                    visit[tx][ty] = visit[x][y] + 1
                    Q.append([tx, ty])
    print(visit[end_x][end_y])


