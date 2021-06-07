import sys; sys.stdin = open('input_data/1389.txt')
from collections import deque

people, num_relations = map(int, input().split())
Ground = [[0]*people for _ in range(people)]
mini = 10000
result = 0
for _ in range(num_relations):
    x, y = map(int, sys.stdin.readline().split())
    Ground[x-1][y-1] = 1
    Ground[y-1][x-1] = 1

for x in range(people):
    bacon = 0
    visit = [0]*people
    visit[x] = 1
    Q = deque()
    Q.append(x)
    while Q:
        i = Q.popleft()
        for j in range(people):
            if not visit[j] and Ground[i][j]:
                Q.append(j)
                visit[j] = visit[i] +1
    if mini > sum(visit):
        mini = sum(visit)
        result = x
print(result+1)