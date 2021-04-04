# import sys
# sys.stdin = open('input/swea_5644_무선충전.txt', 'r')


def charge(ax, ay, bx, by):
    a_charge = [0]*A
    b_charge = [0]*A
    for i in range(A):
        X, Y, C, P = AP[i]
        if abs(ax-X) + abs(ay-Y) <= C:
            a_charge[i] = P
        if abs(bx-X) + abs(by-Y) <= C:
            b_charge[i] = P

    if A == 1: return max(a_charge[0], b_charge[0])
    result = 0
    for i in range(A):
        for j in range(A):
            if i != j:
                result = max(a_charge[i]+b_charge[j], result)
    return result


# 무 상 우 하 좌
dx = [0, 0, 1, 0, -1]
dy = [0, -1, 0, 1, 0]

for tc in range(1, int(input())+1):
    M, A = map(int, input().split()) # M:이동 A: 충전소
    AD = list(map(int, input().split()))
    BD = list(map(int, input().split()))
    AP = [list(map(int, input().split())) for _ in range(A)] # X Y C P

    Ax, Ay = 1, 1
    Bx, By = 10, 10

    ans = charge(Ax, Ay, Bx, By)

    for i in range(M):
        Ax, Ay = Ax + dx[AD[i]], Ay + dy[AD[i]]
        Bx, By = Bx + dx[BD[i]], By + dy[BD[i]]
        ans += charge(Ax, Ay, Bx, By)

    print(f'#{tc} {ans}')