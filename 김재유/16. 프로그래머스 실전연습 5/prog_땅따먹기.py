def solution(lands):
    size = len(lands)
    check = [lands.pop(0)] + [[0]*4 for _ in range(size-1)]
    for idx, land in enumerate(lands, 1):
        check[idx][0] = max(check[idx-1][1], check[idx-1][2], check[idx-1][3]) + land[0]
        check[idx][1] = max(check[idx-1][0], check[idx-1][2], check[idx-1][3]) + land[1]
        check[idx][2] = max(check[idx-1][1], check[idx-1][0], check[idx-1][3]) + land[2]
        check[idx][3] = max(check[idx-1][1], check[idx-1][2], check[idx-1][0]) + land[3]
    return max(check[size-1])