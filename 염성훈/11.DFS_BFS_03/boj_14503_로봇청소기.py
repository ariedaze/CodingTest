import sys
sys.stdin = open("input.txt","r")
from collections import deque

def back(d):
    if d == 0:
        return 2
    elif d == 1:
        return 3
    elif d == 2:
        return 0
    elif d == 3:
        return 1

def checkdir(d):
    if d == 0:
        return 3
    elif d == 1:
        return 0
    elif d == 2:
        return 1
    elif d == 3:
        return 2
def bfs(row, col, d):
    cnt = 1  # 청소하는 칸의 개수
    arr[row][col] = 2
    q = deque([[row, col, d]])

    # 큐가 비어지면 종료
    while q:
        row, col, d = q.popleft()
        temp_d = d

        for i in range(4):
            temp_d = checkdir(temp_d)
            new_row, new_col = row + dy[temp_d], col + dx[temp_d]

            if 0 <= new_row < n and 0 <= new_col < m and arr[new_row][new_col] == 0:
                cnt += 1
                arr[new_row][new_col] = 2
                q.append([new_row, new_col, temp_d])
                break

            elif i == 3:
                new_row, new_col = row + dy[back(d)], col + dx[back(d)]
                q.append([new_row, new_col, d])

                # d
                if arr[new_row][new_col] == 1:
                    return cnt

#시계방향으로 탐색한다.
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m = map(int,input().split())
r, c, d = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

print(bfs(r,c,d))

