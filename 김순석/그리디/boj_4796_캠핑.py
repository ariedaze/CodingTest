import sys
In = sys.stdin.readline

t = 0
while True:
    result = 0
    t += 1
    L, P, V = map(int, In().split())
    if L == P == V == 0:
        break

    Q = V // P
    R = V % P

    # input이 2 8 20 일때 생각해보기
    if R > L:
        R = L
    result = (L * Q) + R
    # print(L, P, V)
    print('Case {}: {}'.format(t, result))