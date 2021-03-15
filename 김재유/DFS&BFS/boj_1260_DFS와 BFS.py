import sys; sys.stdin = open('input_data/1260.txt')

def DFS(now):
    print(now, end=' ')
    visit[now] = 1
    for i in line_data[now]:
        if not visit[i]:
            DFS(i)

def BFS():
    while Q:
        now = Q.pop(0)
        if visit[now]:
            continue
        print(now, end=' ')
        visit[now] = 1
        for i in line_data[now]:
            if not visit[i]:
                Q.append(i)

dot, line, start = map(int, input().split())
line_data = [[] for _ in range(dot+1)]

visit = [0]*(dot+1)
for _ in range(line):
    x, y = map(int, input().split())
    line_data[x].append(y)
    line_data[y].append(x)
for data in line_data:
    data.sort()
DFS(start)
print()
visit = [0]*(dot+1)
Q = [start]
BFS()