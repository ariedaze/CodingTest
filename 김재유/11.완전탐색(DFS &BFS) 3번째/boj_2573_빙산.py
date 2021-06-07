import sys; sys.stdin = open("input_data/2573.txt")
sys.setrecursionlimit(100000)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def melting(x, y):
    global total
    global check
    check += 1
    visit[x][y] = 1
    melt = 0
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < height and 0 <= ty < width and not Ground[tx][ty]:
            melt += 1

    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if 0 <= tx < height and 0 <= ty < width and Ground[tx][ty] and not visit[tx][ty]:
            melting(tx, ty)
    Ground[x][y] = max(0, Ground[x][y] - melt)
    if not Ground[x][y]:
        total -= 1

height, width = map(int, sys.stdin.readline().split())
Ground = []
origin_total = 0
result = -1
for _ in range(height):
    line = list(map(int, sys.stdin.readline().split()))
    Ground.append(line)
    origin_total += len(list(filter(lambda x: x != 0, line)))

keep_going = True
while keep_going:
    result += 1
    checking = False
    visit = [[0]*width for _ in range(height)]
    if not origin_total:
        keep_going = False
        print('0')
        break
    for i in range(height):
        for j in range(width):
            if Ground[i][j]:
                total = int(origin_total)
                check = 0
                melting(i, j)
                if check != origin_total:
                    keep_going = False
                origin_total = total
                checking = True
                break
        if checking:
            break
else:
    print(result)