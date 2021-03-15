# 어거지로 품
# 최소 time 구한 후 ans에 집어넣고 그 다음 time 값을 구하기 전까지 v==k인 경우 카운트해주고 다음 depth(time)으로 가면 리턴함

import sys
from collections import deque
# sys.stdin = open('input/boj_12851_숨바꼭질 2.txt', 'r')
In = sys.stdin.readline

N, K = map(int, In().split())
visit = [0xfffff] * (10 ** 5 + 1)


def bfs(v, k):
    global cnt, ans, time
    q = deque()
    q.append((v, 0))

    while q:
        v, time = q.popleft()

        if v == k:
            if time > ans:
                return
            else:
                ans = time
                cnt += 1

        if time < visit[v]:
            visit[v] = time

        time += 1
        calc = [v*2, v+1, v-1]
        for i in calc:
            if 0 <= i <= 100000 and visit[i] >= time:
                q.append((i, time))


cnt = 0
time = 0
ans = 0xfffff
bfs(N, K)
print(ans)
print(cnt)