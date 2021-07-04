n = 5

def solution(n):
    total = sum([i for i in range(n+1)])
    tower = [[0] * i for i in range(1, n+1)]
    i = 0
    left = 0
    right = 0
    floor = -1
    while True:
        count = 0
        while count != n:
            i += 1
            floor += 1
            count += 1
            tower[floor][left] = i
        left += 1
        count = 0
        n -= 1
        if i == total:
            break
        while count != n:
            right += 1
            i += 1
            count += 1
            tower[floor][right] = i
        count = 0
        n -= 1
        if i == total:
            break
        while count != n:
            floor -= 1
            right -= 1
            i += 1
            count += 1
            tower[floor][right] = i
        count = 0
        n -= 1
        if i == total:
            break
    result = []
    for floor in tower:
        result += floor
    return result




