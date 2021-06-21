# import sys
# sys.stdin = open('input/게임 맵 최단거리.txt', 'r')

from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(maps):
    row = len(maps)
    col = len(maps[0])
    memo = [[0 for _ in range(col)] for _ in range(row)]
    memo[0][0] = 1
    
    queue = deque()
    queue.append([0,0,1])
    
    while queue:
        r, c, d = queue.popleft()
        
        for i in range(4):
            dr, dc = r + dx[i], c + dy[i]
            if 0 <= dr < row and 0 <= dc < col and maps[dr][dc] == 1 and memo[dr][dc] == 0:
                if dr == row-1 and dc == col-1:
                    return d + 1
                memo[dr][dc] = d + 1
                queue.append([dr, dc, d + 1])
        
    return -1

def solution(maps):
    return bfs(maps)