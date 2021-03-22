import sys
sys.stdin = open("input.txt","r")
from collections import deque

T = int(input())

tunnel = {
    0: (),
    1: ((1, 0), (0, 1), (-1, 0), (0, -1)),
    2: ((1, 0), (-1, 0)),
    3: ((0, 1), (0, -1)),
    4: ((-1, 0), (0, 1)),
    5: ((1, 0), (0, 1)),
    6: ((1, 0), (0, -1)),
    7: ((-1, 0), (0, -1))
}

for t in range(1,T + 1):
    N, M, R, C, L = map(int,input().split()) #R,C : 맨홀 뚜껑 위치 N: x, M : y
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    visited[R][C], cnt = 1, 1
    Q = deque([(R,C)])
    while Q:
        x, y = Q.popleft()
        for dx, dy in tunnel[arr[x][y]]:
            tx, ty = x+dx, y+dy

            if tx < 0 or tx == N or ty < 0 or ty == M:
                continue
            if (-dx, -dy) in tunnel[arr[tx][ty]]:
                if not visited[tx][ty]:
                    visited[tx][ty] = visited[x][y] + 1
                    Q.append((tx,ty))
                    if visited[tx][ty] <= L:
                        cnt += 1

    print("#{} {}".format(t,cnt))




