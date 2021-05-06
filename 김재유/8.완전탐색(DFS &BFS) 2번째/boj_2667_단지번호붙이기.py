import sys
from pprint import pprint

sys.stdin = open('input_data/2667.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def DSF(x, y):
    global count
    count += 1
    visit[x][y] = 1
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < size and 0 <= ty < size and ground[tx][ty] and not visit[tx][ty]:
            DSF(tx,ty)


size = int(input())
ground = [list(map(int, ' '.join(input()).split())) for _ in range(size)]

visit = [[0] * size for _ in range(size)]
count_list = []
for x in range(size):
    for y in range(size):
        if ground[x][y] and not visit[x][y]:
            count = 0
            DSF(x, y)
            count_list.append(count)

print(len(count_list))
for count in sorted(count_list):
    print(count)
