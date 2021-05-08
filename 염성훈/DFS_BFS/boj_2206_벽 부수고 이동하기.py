import sys
from collections import deque
sys.stdin = open("input.txt","r")

# 처음 생각 했던건 벽을 하나씩 부수고 매번 bfs를 돌리면 시간 초과 떄문에 안된다.
# 3차원 리스트를 활용해야한다.
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append([0,0,0])
    visited[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if tx < 0 or tx == N or ty < 0 or ty == M:
                continue
            #벽을 뚫은 배열이면 bfs계속실행
            if arr[tx][ty] == 0 and visited[tx][ty][z] == -1:
                visited[tx][ty][z] = visited[x][y][z] + 1
                q.append([tx,ty, z])
            #벽을 뚫지 않았고 다음 열에 벽이 있을 경우에
            elif z == 0 and arr[tx][ty] == 1 and visited[tx][ty][z + 1] == -1:
                visited[tx][ty][z + 1] = visited[x][y][z] + 1
                q.append([tx,ty, z + 1])



N, M = map(int,input().split())

arr = [list(map(int,input())) for _ in range(N)]
visited = [[[-1] * 2 for _ in range(M)] for _ in range(N)]
bfs()
ans1, ans2 = visited[N-1][M-1][0], visited[N-1][M-1][1]
if ans1 == -1 and ans2 != -1:
    print(ans2)
elif ans1 != -1 and ans2 == -1:
    print(ans1)
else:
    print(min(ans1, ans2))




