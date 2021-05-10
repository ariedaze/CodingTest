import sys
sys.stdin = open('input/boj_2468_안전 영역.txt', 'r')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(idx, h):
    stack = []
    stack.append(idx)
    while stack:
        r, c = stack.pop()
        for i in range(4):
            tr, tc = r + dr[i], c + dc[i]
            if 0 <= tr < N and 0 <= tc < N and matrix[tr][tc] > h and visit[tr][tc] == False:
                stack.append([tr,tc])
                visit[tr][tc] = True


N = int(input())

matrix = []
num_li = []
visit = [[False for _ in range(N)] for _ in range(N)]
max_num = 1  #

for i in range(N):
    data = list(map(int, input().split()))
    matrix.append(list(data))
    num_li += data

for i in set(num_li):
    count = 0
    visit = [[False for _ in range(N)] for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if matrix[j][k] > i and visit[j][k] == False:
                visit[j][k] = True
                dfs([j,k],i)
                count += 1
    if count > max_num:
        max_num = count

print(max_num)