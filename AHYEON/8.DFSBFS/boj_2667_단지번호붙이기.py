from collections import deque


N = int(input())
graph = [input() for _ in range(N)]

answer = []
visited = [[0]*N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == '1':
            Q = deque([(i, j)])
            visited[i][j] = 1
            cnt = 1
            while Q:
                v = Q.popleft()
                for mode in range(4):
                    nx = v[0] + dx[mode]
                    ny = v[1] + dy[mode]
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == '1':
                        Q.append([nx, ny])
                        visited[nx][ny] = 1
                        cnt += 1
            answer.append(cnt)

print(len(answer))
answer.sort()
for a in answer:
    print(a)


