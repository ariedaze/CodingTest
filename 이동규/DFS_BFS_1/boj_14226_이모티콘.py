import sys
sys.stdin = open('input/boj_14226_이모티콘.txt', 'r')

from collections import deque

def dfs(info):
    global MIN

    queue = deque()
    queue.append(info)

    while queue:
        n, c, clip = queue.popleft()

        if n == target and c < MIN:
            MIN = c
            continue

        for i in range(2):
            if i == 0 and n * 2 < 1001 and visit[n * 2] > c:
                visit[n * 2] = c + 2
                queue.append([n * 2, c + 2, clip + n])
            elif i == 1 and n + clip <= target and visit[n + clip] > c:
                visit[n + clip] = c + 1
                queue.append([n + clip, c + 1, clip])


target = int(input())
MIN = 1001
visit = [1001 for _ in range(100001)]
visit[1] = 0

dfs([1, 0, 0])

print(MIN)