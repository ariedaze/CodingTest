def solution(n):
    #이등변 직각삼각형만들기
    tri = [[0 for i in range(0, j)] for j in range(1, n + 1)]
    # 숫자 채우기
    # 행
    x = -1
    # 열
    y = 0
    k = 1

    for a in range(n):
        # 열 접근
        for b in range(a, n):
            if a % 3 == 0:
                x += 1
            elif a % 3  == 1:
                y += 1
            elif a % 3 == 2:
                x -= 1
                y -= 1
            tri[x][y] = k
            k += 1

    answer = sum(tri, [])
    return answer
