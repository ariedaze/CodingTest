import sys
sys.stdin = open('input/boj_2206_벽 부수고 이동하기.txt', 'r')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    global MD
    visit = [[[1000000] * 2 for _ in range(M)] for _ in range(N)]
    visit[0][0][0] = 0

    queue = deque()
    queue.append([0, 0, 0])

    while queue:
        r, c, is_smashed = queue.popleft()

        if r == N - 1 and c == M - 1:
            if MD > visit[r][c][is_smashed]:
                MD = visit[r][c][is_smashed]

        for i in range(4):
            tr, tc = r + dx[i], c + dy[i]
            if 0 <= tr < N and 0 <= tc < M and visit[tr][tc][is_smashed] > visit[r][c][is_smashed] + 1 and matrix[tr][tc] == 0:
                visit[tr][tc][is_smashed] = visit[r][c][is_smashed] + 1
                queue.append([tr, tc, is_smashed])
            if 0 <= tr < N and 0 <= tc < M and visit[tr][tc][is_smashed] > visit[r][c][is_smashed] + 1 and matrix[tr][tc] == 1 and is_smashed == False:
                visit[tr][tc][1] = visit[r][c][is_smashed] + 1
                queue.append([tr, tc, 1])


N, M = list(map(int, input().split()))
matrix = []
MD = 9999999 # minimum distance

for i in range(N):
    matrix.append(list(map(int, list(input()))))

bfs()

if MD == 9999999:
    print(-1)
else:
    print(MD+1)