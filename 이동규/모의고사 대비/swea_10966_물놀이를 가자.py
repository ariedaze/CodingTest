import sys
sys.stdin = open('input/swea_10966_물놀이를 가자.txt', 'r')
from collections import deque

dx, dy = [-1, 1, 0 ,0], [0 ,0, -1, 1]

def bfs(index):
    temp_visit = visit.copy()
    temp_min = 9999999
    queue = deque()
    queue.append(index)
    temp_visit[index[0]][index[1]] = 0
    while queue and queue[0][2] < temp_min:
        tr, tc, d = queue.popleft()
        for i in range(4):
            dr, dc = tr + dx[i], tc + dy[i]
            if 0 <= dr < R and 0 <= dc < C and temp_visit[dr][dc] > d:
                temp_visit[dr][dc] = d + 1
                if MAP[dr][dc] == 'L':
                    queue.append([dr, dc, d + 1])
                if MAP[dr][dc] == 'W' and temp_min > d + 1:
                    temp_min = d + 1

    return temp_min


for T in range(1, int(input())):
    R, C = list(map(int, input().split()))
    MAP = [list(input()) for i in range(R)]
    visit = [[9999999 for _ in range(C)] for _ in range(R)]
    sum = 0

    for r in range(R):
        for c in range(C):
            if MAP[r][c] == 'L':
                sum += bfs([r, c, 0])

    print(sum)