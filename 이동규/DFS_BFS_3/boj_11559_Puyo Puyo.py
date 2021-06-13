import sys
sys.stdin = open('input/boj_11559_Puyo Puyo.txt', 'r')

from collections import deque
from operator import itemgetter

dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

def dfs(info):
    stack = deque()
    stack.append(info)

    temp = []

    while stack:
        row, col, char = stack.pop()
        temp.append([row, col])
        for i in range(4):
            dr, dc = row + dx[i], col + dy[i]
            if 0 <= dr < 6 and 0 <= dc < 12 and MY_MAP[dr][dc] == char and visit[dr][dc] == False:
                visit[dr][dc] = True
                stack.append([dr, dc, char])

    if len(temp) > 3:
        return temp


MAP = [list(input()) for _ in range(12)]
MAP = list(zip(*MAP))

MY_MAP = []
cycle = 0

for tpl in MAP:
    MY_MAP.append(list(tpl)[::-1])

while True:
    delete_targets = []

    visit = [[False for _ in range(12)] for _ in range(6)]

    for r in range(6):
        for c in range(12):
            if MY_MAP[r][c] != '.':
                visit[r][c] = True
                delete_target = dfs([r, c, MY_MAP[r][c]])
                if delete_target:
                    delete_targets.extend(delete_target)

    if delete_targets:
        cycle += 1

        delete_targets.sort(key=itemgetter(0,1))

        for del_r, del_c in delete_targets[::-1]:
            MY_MAP[del_r].pop(del_c)
            MY_MAP[del_r].append('.')
    else:
        break

print(cycle)




