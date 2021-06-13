import sys
sys.stdin = open('boj_16928.txt', 'r')

import sys
from collections import deque
readline = sys.stdin.readline

N, M = map(int, readline().split())

fields = [0 for _ in range(101)]
visited = [0 for _ in range(101)]

for _ in range(N + M):
    s, e = map(int, readline().split())
    fields[s] = e

Q = deque([(1, 0)])
min_res = 0xffffff
while Q:
    c, res = Q.popleft()

    for add in range(1, 7):
        n_c = c + add
        if n_c > 99:
            Q.clear()
            min_res = res + 1
            break

        if not visited[n_c]:
            visited[n_c] = 1
            if fields[n_c]:
                Q.append((fields[n_c], res + 1))
            else:
                Q.append((n_c, res + 1))

print(min_res)