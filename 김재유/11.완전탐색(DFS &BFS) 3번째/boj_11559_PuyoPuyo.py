import sys; sys.stdin = open('input_data/11559.txt')
from pprint import pprint

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
height = 12
width = 6

def Puyo(x, y, color):
    global count
    pang.append([x, y])
    visit[x][y] = 1
    cut_line.add(y)
    count += 1
    for r in range(4):
        tx = x + dx[r]
        ty = y + dy[r]
        if 0 <= tx < 12 and 0 <= ty < 6 and Ground[tx][ty] == color and [tx, ty] not in pang:
            Puyo(tx, ty, color)

def gravity(j):
    one_line = [Ground[i][j] for i in range(12)]
    moved = list(filter(lambda x: x != ".", one_line))
    moved = ["."]*(12-len(moved)) + moved
    for x in range(12):
        Ground[x][j] = moved[x]

Ground = [list(' '.join(input()).split()) for _ in range(height)]
result = 0
keep_going = True
while keep_going:
    result += 1
    keep_going = False
    total_pang = []
    total_cut_line = set()
    visit = [[0]*width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            if Ground[i][j] != "." and not visit[i][j]:
                pang = []
                cut_line = set()
                count = 0
                Puyo(i, j, Ground[i][j])
                if count >= 4:
                    total_pang += pang
                    total_cut_line.update(cut_line)
                    keep_going = True
                    for block in pang:
                        Ground[block[0]][block[1]] = "."
    for x in total_cut_line:
        gravity(x)
pprint(Ground)
print(result)