commend = {
    "U" : (-1, 0),
    "L" : (0, -1),
    "R" : (0, 1),
    "D" : (1, 0),
}

def solution(dirs):
    answer = 0
    maps = [[0] * 11 for _ in range(11)]
    x, y = 5, 5
    check = set()
    for dir in dirs:
        moveX, moveY = commend[dir]

        if 0 <= x + moveX <= 10 and 0 <= y + moveY <= 10:
            tx, ty = x + moveX, y + moveY
            #뒤로 갈 수 있기 떄문이다.
            if (x, y, tx, ty) not in check:
                check.add((x, y, tx, ty))
                check.add((tx, ty, x, y)) #길이 양방향이기 떄문에 두번해줘야한다.
                answer += 1
            x, y = tx, ty
    return answer

dirs = "ULURRDLLU"
solution(dirs)
