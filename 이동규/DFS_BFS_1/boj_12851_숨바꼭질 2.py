import sys
sys.stdin = open('input/boj_12851_숨바꼭질 2.txt', 'r')
from collections import deque

def dfs(info):
    global MIN, duplicat_num

    queue = deque()
    queue.append(info)

    while queue:
        n, c = queue.popleft()

        if n == B and c < MIN:
            MIN = c
            duplicat_num = 1
            continue
        if n == B and c == MIN:
            duplicat_num += 1
            continue

        for i in range(3):
            if i == 0 and n * 2 < 100001 and visit[n * 2] > c:
                visit[n * 2] = c + 1
                queue.append([n * 2, c + 1])
            elif i == 1 and n + 1 <= B and visit[n + 1] > c:
                visit[n + 1] = c + 1
                queue.append([n + 1, c + 1])
            elif i == 2 and 0 <= n - 1 and visit[n - 1] > c:
                visit[n - 1] = c + 1
                queue.append([n - 1, c + 1])

A, B = list(map(int, input().split()))
MIN = 100001
visit = [100001 for _ in range(100001)]
visit[A] = 0
duplicat_num = 1

dfs([A, 0])

print(MIN)
print(duplicat_num)