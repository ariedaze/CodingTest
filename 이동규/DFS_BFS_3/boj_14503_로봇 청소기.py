import sys
# sys.stdin = open('input/boj_14503_로봇 청소기.txt', 'r')
sys.setrecursionlimit(99999)

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

def step1(info):
    global total, exit_flag

    if exit_flag:
        return

    r, c, d = info
    MAP[r][c] = 2
    total += 1
    step2(info)

def step2(info):
    global exit_flag

    if exit_flag:
        return
    r, c, d = info

    ld = (d+3) % 4
    lr, lc = r + dx[ld], c + dy[ld]

    bd = (d+2) % 4
    br, bc = r + dx[bd], c + dy[bd]

    is_isolate = True

    for i in range(4):
        dr, dc = r + dx[i], c + dy[i]
        if 0 <= dr < R and 0 <= dc < C and MAP[dr][dc] == 0:
            is_isolate = False

    if is_isolate:
        if MAP[br][bc] == 1:
            exit_flag = 1
        else:
            step2([br, bc, d])

    if 0 <= lr < R and 0 <= lc < C and MAP[lr][lc] == 0:
        step1([lr, lc, ld])
    elif 0 <= lr < R and 0 <= lc < C and MAP[lr][lc]:
        step2([r, c, ld])


R, C = list(map(int, input().split()))
X, Y, D = list(map(int, input().split()))
MAP = [list(map(int, input().split())) for _ in range(R)]
total = 0
exit_flag = 0

step1([X, Y, D])

print(total)