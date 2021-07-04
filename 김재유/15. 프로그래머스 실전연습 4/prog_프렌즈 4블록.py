from pprint import pprint

def kill(x, y, Ground):
    if Ground[x][y] and Ground[x][y] == Ground[x + 1][y] == Ground[x][y + 1] == Ground[x + 1][y + 1]:
        return [[x, y], [x + 1, y], [x, y + 1], [x + 1, y + 1]]
    return []

def gravity(y, height, Ground):
    for i in range(height - 1, 1, -1):
        if not Ground[i][y]:
            for j in range(i-1, -1, -1):
                if Ground[j][y]:
                    Ground[i][y], Ground[j][y] = Ground[j][y], Ground[i][y]
                    break
    return Ground

def solution(height, width, boards):
    result = 0
    Ground = []
    for board in boards:
        Ground.append(list(" ".join(board).split()))
    while True:
        change = []
        for i in range(height - 1):
            for j in range(width - 1):
                change += kill(i, j, Ground)
        if change:
            cut_line = []
            for x, y in change:
                if Ground[x][y]:
                    Ground[x][y] = 0
                    result += 1
                if y not in cut_line:
                    cut_line.append(y)
            for cut in cut_line:
                Ground = gravity(cut, height, Ground)
        else:
            return result

print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))