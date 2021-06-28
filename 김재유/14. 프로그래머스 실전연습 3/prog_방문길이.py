dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
navi = {
    "U": 0,
    "R": 1,
    "D": 2,
    "L": 3
}
mirror = {
    "U": "D",
    "R": "L",
    "D": "U",
    "L": "R"
}


def solution(dirs):
    result = 0
    before = [[""] * 11 for _ in range(11)]
    x, y = 5, 5
    for i in dirs:
        tx = x + dx[navi[i]]
        ty = y + dy[navi[i]]
        if 0 <= tx < 11 and 0 <= ty < 11:
            if not before[tx][ty].count(i):
                result += 1
                before[tx][ty] += i
                before[x][y] += mirror[i]
            x, y = tx, ty

    return result