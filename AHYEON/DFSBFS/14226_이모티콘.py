from collections import deque

S = int(input())
visited = [[-1]*(S+1) for _ in range(S+1)]
visited[1][0] = 0  # 화면에 한개
Q = deque([(1, 0)])

while Q:
    # 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
    # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
    # 3. 화면에 있는 이모티콘 중 하나를 삭제한다.
    s, c = Q.popleft()  # s: 화면, c: 클립보드
    if visited[s][s] == -1:
        visited[s][s] = visited[s][c] + 1  # 1. 복사 (s,c) => (s, s)
        Q.append((s, s))
    if s + c <= S and visited[s+c][c] == -1:
        visited[s+c][c] = visited[s][c] + 1  # 2. 붙여넣기 (s, s) => (s+c, c)
        Q.append((s+c, c))
    if s-1>= 0 and visited[s-1][c] == -1:
        visited[s-1][c] = visited[s][c] + 1  # 3. 삭제 (s. s) => (s-1, c)
        Q.append((s-1, c))


ans = -1
for i in range(S+1):
    if visited[S][i] != -1:
        if ans == -1 or ans > visited[S][i]:
            ans = visited[S][i]


print(ans)
