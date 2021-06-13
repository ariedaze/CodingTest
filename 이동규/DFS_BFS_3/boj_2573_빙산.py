import sys
sys.stdin = open('input/boj_2573_빙산.txt', 'r')

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def melting():
    global iceland

    new_iceland = []
    melting_count = []

    for spot in iceland:
        r, c = spot
        tmp = 0

        for i in range(4):
            dr, dc = r + dx[i], c + dy[i]
            if 0 <= dr < R and 0 <= dc < C and MAP[dr][dc] == 0:
                tmp += 1

        melting_count.append(tmp)

        if MAP[r][c] - tmp > 0:
            new_iceland.append([r, c])

    for j, i in enumerate(melting_count):
        x, y = iceland[j]
        MAP[x][y] = MAP[x][y] - i if MAP[x][y] - i > 0 else 0

    iceland = new_iceland


def dfs():
    if len(iceland):
        visit = [[False for _ in range(C)] for _ in range(R)]
        visit[iceland[0][0]][iceland[0][1]] = True
        stack = [iceland[0]]
        count = 1

        while stack:
            r, c = stack.pop()

            for i in range(4):
                dr, dc = r + dx[i], c + dy[i]
                if 0 <= dr < R and 0 <= dc < C and MAP[dr][dc] != 0 and visit[dr][dc] == False:
                    visit[dr][dc] = True
                    stack.append([dr, dc])
                    count += 1

        return count != len(iceland)

R, C = list(map(int, input().split()))
MAP = [list(map(int, input().split())) for _ in range(R)]
iceland = []
year = 1

for r in range(R):
    for c in range(C):
        val = MAP[r][c]
        if val:
            iceland.append([r, c])

while iceland:
    melting()
    if dfs():
        print(year)
        break
    year += 1

if not iceland:
    print(0)
