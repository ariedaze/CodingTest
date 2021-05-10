import sys
sys.stdin = open('input/boj_7569_토마토.txt', 'r')

import collections


dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]


def bfs():
    global max_day
    while queue:
        d, sa, sr, sc = queue.popleft()
        if max_day < d:
            max_day = d
        for k in range(6):
            td, ta, tr, tc = d + 1, sa + dz[k], sr + dx[k], sc + dy[k]
            if 0 <= tr < row and 0 <= tc < col and 0 <= ta < ais and matrix[ta][tr][tc] == 0:
                matrix[ta][tr][tc] = td
                queue.append([td, ta, tr, tc])


col, row, ais = list(map(int, input().split())) # 열, 행, 층
matrix = []
queue = collections.deque()
max_day = 0

for a in range(ais):
    matrix.append([])
    for r in range(row):
        matrix[a].append(list(map(int, input().split())))
        for c in range(col):
            if matrix[a][r][c] == 1:
                queue.append([0, a, r, c])
bfs()

for i in matrix:
    for j in i:# 안익은 토마토가 갇혀있는 경우
        if 0 in j:
            max_day = -1
            break

print(max_day)