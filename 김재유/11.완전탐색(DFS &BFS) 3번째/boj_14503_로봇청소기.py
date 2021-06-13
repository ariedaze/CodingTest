import sys; sys.stdin = open('input_data/14503.txt')
sys.setrecursionlimit(100000)
from pprint import pprint
from collections import deque

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def cleanup(i,j):
    global result
    result += 1
    Ground[i][j] = 2

def check_around(x, y):
    for idx in range(4):
        tx = x + dx[idx]
        ty = y + dy[idx]
        # 주변에 청소할 곳이 있다면?
        if not Ground[tx][ty]:
            return False
    else:
        return True

# 왼쪽 좌표 구하기
def address(x, y, idx):
    tx = x + dx[idx]
    ty = y + dy[idx]
    return [tx, ty]

# def next_search(x, y, way):
#     cleanup(x, y)
#     left_x, left_y = address(x, y, way)
#     next_way = way-1
#     back_way = way-2
#     if next_way < 0:
#         next_way = 3
#     if back_way < 0:
#         back_way = 4 + back_way
#     back_x, back_y = address(x, y, next_way)
#
#     if check_around(x, y):
#         if Ground[back_x][back_y] == 1:
#             return
#         else:
#             next_search(back_x, back_y, back_way)
#     elif not Ground[left_x][left_y]:
#         next_search(left_x, left_y, next_way)
#     else:
#         next_search(x, y, next_way)

height, width = map(int, input().split())
result = 0
# 0 : 북, 1 : 동,  2 : 남, 3: 서
robot_x, robot_y, compass = map(int, input().split())
Ground = [list(map(int, input().split())) for _ in range(height)]
# next_search(robot_x, robot_y, compass)
Q = deque()
Q.append([robot_x, robot_y, compass])
while Q:
    x, y, way = Q.popleft()
    if not Ground[x][y]:
        cleanup(x, y)
    left_x, left_y = address(x, y, way)
    next_way = way-1
    back_way = way-2
    if next_way < 0:
        next_way = 3
    if back_way < 0:
        back_way = 4 + back_way
    back_x, back_y = address(x, y, next_way)

    if check_around(x, y):
        if Ground[back_x][back_y] == 1:
            pass
        else:
            Q.append([back_x, back_y, way])
    elif not Ground[left_x][left_y]:
        Q.append([left_x, left_y, next_way])
    else:
        Q.append([x, y, next_way])

print(result)

