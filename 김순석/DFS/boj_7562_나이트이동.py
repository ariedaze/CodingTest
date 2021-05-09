from collections import deque

# 1시 방향 부터
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

T = int(input())
for t in range(1, T + 1):
    # 배열 크기
    N = int(input())
    # 시작점
    x, y = map(int, input().split())
    # 도착점
    ex, ey = map(int, input().split())


    q = deque()
    q.append((x, y))
    memo = [[0] * N for _ in range(N)]
    memo[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == ex and y == ey: break
        for i in range(8):
            tx, ty = x + dx[i], y + dy[i]
            if tx < 0 or tx >= N or ty < 0 or ty >= N or memo[tx][ty]: continue

            memo[tx][ty] = memo[x][y] + 1
            q.append((tx, ty))

    print(memo[ex][ey] - 1)