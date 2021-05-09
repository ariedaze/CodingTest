import sys
from collections import deque

ln = sys.stdin.readline


def D(x):
    x = (2 * x) % 10000
    return x


def S(x):
    return 9999 if x == 0 else x - 1


def L(x):
    return int((x % 1000) * 10 + x / 1000)


def R(x):
    return int((x % 10) * 1000 + x / 10)


def bfs(x, y, ans):
    q.append([x, ans])
    while q:
        x, ans = q.popleft()
        for i in range(4):
            if i == 0:
                tx = D(x)
                if visit[tx] == 0:
                    visit[tx] = 1
                    q.append([tx, ans + 'D'])
                if tx == y:
                    return ans + 'D'
            elif i == 1:
                tx = S(x)
                if visit[tx] == 0:
                    visit[tx] = 1
                    q.append([tx, ans + 'S'])
                if tx == y:
                    return ans + 'S'

            elif i == 2:
                tx = L(x)
                if visit[tx] == 0:
                    visit[tx] = 1
                    q.append([tx, ans + 'L'])
                if tx == y:
                    return ans + 'L'

            elif i == 3:
                tx = R(x)
                if visit[tx] == 0:
                    visit[tx] = 1
                    q.append([tx, ans + 'R'])
                if tx == y:
                    return ans + 'R'


T = int(ln())
for t in range(1, T + 1):
    A, B = map(int, ln().split())
    ans = ''
    q = deque()
    visit = [0 for _ in range(10000)]
    print(bfs(A, B, ans))

