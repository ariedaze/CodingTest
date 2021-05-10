import sys

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

sys.setrecursionlimit(10**8)


def dfs(x, y, cnt, part_sum):
    global ans, flag
    # 부분 합이 답보다 크다면 종료
    if part_sum > ans:
        return
    # 3에 도착한다면 답 계산
    if (x, y) == end:
        flag = True
        ans = min(part_sum, ans)
        return

    for mode in range(4):
        nx, ny = x + dx[mode], y + dy[mode]
        if 0 <= nx < N and 0 <= ny < M:
            if miro[nx][ny] == '1' and cnt == 0 and not visited[nx][ny]:
                dfs(nx, ny, cnt + 1, part_sum + 1)

            elif miro[nx][ny] != '1' and not visited[nx][ny]:
                visited[nx][ny] = 1
                dfs(nx, ny, cnt, part_sum+1)
                visited[nx][ny] = 0


N, M = map(int, sys.stdin.readline().split())
miro = [list(sys.stdin.readline()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
ans = N*M
flag = False

start = (0, 0)
end = (N-1, M-1)

visited[start[0]][start[1]] = 1
dfs(start[0], start[1], 0, 1)

if flag:
    print('{}'.format(ans))
else:
    print(-1)