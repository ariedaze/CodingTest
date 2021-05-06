import sys
sys.setrecursionlimit(1000000)
sys.stdin = open('input_data/11724.txt')

def DSF(x):
    visit[x]= 1
    for i in range(1, dot+1):
        if ground[x][i] and not visit[i]:
            DSF(i)

dot, line = map(int,input().split())
line_data = [list(map(int,sys.stdin.readline().split())) for _ in range(line)]
ground = [[0]*(dot+1) for _ in range(dot+1)]
for data in line_data:
    ground[data[0]][data[1]] = 1
    ground[data[1]][data[0]] = 1

visit = [0]*(dot+1)
count = 0
while visit.count(0) != 1:
    for x in range(1, dot+1):
        if not visit[x]:
            DSF(x)
            count += 1
print(count)

