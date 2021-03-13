import sys
sys.stdin = open('input/boj_1260_DFS와 BFS.txt', 'r')

from collections import deque

def dfs(node):
    V[node] = True
    print(node+1, end=' ')
    for i in range(N):
        if matrix[node][i] and V[i] == False:
            dfs(i)

def bfs(node):
    queue = []
    queue.append(node)
    V[node] = True

    while queue:
        row = queue.pop(0)
        print(row + 1, end=' ')

        for i in range(N):
            if matrix[row][i] and V[i] == False:
                queue.append(i)
                V[i] = True


N, E, S = list(map(int, input().split()))
V = [False for _ in range(N)]
matrix = [[0 for _ in range(N)] for _ in range(N)]

for i in range(E):
    r, c = list(map(int, input().split()))
    matrix[r-1][c-1] = matrix[c-1][r-1] = 1

dfs(S-1)
print()

V = [False for _ in range(N)]
bfs(S-1)

