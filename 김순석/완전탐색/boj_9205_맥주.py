import sys
from collections import deque

ln = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append([x, y])
    tmp = [[x, y]]

    while q:
        x, y = q.popleft()
        if x == end_x and y == end_y:
            print('happy')
            return

        for tx, ty in lst:
            if [tx, ty] not in tmp:
                k = abs(tx - x) + abs(ty - y)
                if 1000 >= k:
                    q.append([tx, ty])
                    tmp.append([tx, ty])
    print('sad')
    return


T = int(ln())
for t in range(T):
    n = int(ln())
    start_x, start_y = map(int, ln().split())
    lst = []
    for i in range(n):
        x, y = map(int, ln().split())
        lst.append([x, y])
    end_x, end_y = map(int, ln().split())

    lst.append([end_x, end_y])
    bfs(start_x, start_y)
