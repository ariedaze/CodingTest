def dfs(x, y, mode, cnt, k):
    global time, K, x2, y2, ans
    if time < cnt:
        return
    if x == x2 and y == y2:
        # print('무야호', cnt)
        ans = True
        time = min(cnt, time)
        return

    nx, ny = x + dx[mode], y + dy[mode]
    k -= 1

    if k and 0 <= nx < N and 0 <= ny < M and gym[nx][ny] == '.' and not visited[nx][ny]:  # 같은 방향으로 갈 수 있다면?
        visited[nx][ny] = 1
        dfs(nx, ny, mode, cnt, k)
        visited[nx][ny] = 0
    else:  # 새로 방향 전환 필요
        for new_mode in range(4):
            nx, ny = x + dx[new_mode], y + dy[new_mode]
            if 0 <= nx < N and 0 <= ny < M and gym[nx][ny] == '.' and not visited[nx][ny]:
                cnt += 1  # 방향 전환해서 +1
                k = K
                visited[nx][ny] = 1
                dfs(nx, ny, new_mode, cnt, k)
                visited[nx][ny] = 0


N, M, K = map(int, input().split())
gym = [input() for _ in range(N)]
x1, y1, x2, y2 = map(int, input().split()); x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
visited = [[0]*M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ans = False
time = 100000000000
visited[x1][y1] = 1


dfs(x1, y1, 0, 0, K)


if ans:
    print(time)
else:
    print(-1)

