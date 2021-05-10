import sys
sys.stdin = open('input/boj_7562_나이트의 이동.txt', 'r')

from collections import deque

dx, dy = [2, 1, -1, -2, -2, -1, 1, 2], [1, 2, 2, 1, -1, -2, -2, -1]

def bfs():
    queue = deque()
    queue.append(S)

    while queue:
        r, c = queue.popleft()
        for i in range(8):
            dr, dc = r + dx[i], c + dy[i]
            if 0 <= dr < N and 0 <= dc < N and M[dr][dc] > M[r][c] + 1:
                M[dr][dc] = M[r][c] + 1
                queue.append([dr, dc])

for T in range(1, int(input())+1):
    N = int(input())
    M = [[1000000 for _ in range(N)] for _ in range(N)]
    S, D= list(map(int, input().split())), list(map(int, input().split()))
    M[S[0]][S[1]] = 0
    bfs()
    print(M[D[0]][D[1]])