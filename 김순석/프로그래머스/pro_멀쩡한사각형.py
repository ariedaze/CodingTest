from math import gcd, ceil


def solution(w, h):
    answer = w * h
    if w > h:
        h, w = w, h

    k = gcd(w, h)
    x, y = h / k, w / k

    answer -= ceil(x / y) * k

    cnt = 2
    while cnt <= y:
#         나눗셈 연산 순서 조심
        tmp1 = ceil((x * (cnt - 1)) / y)
        tmp2 = ceil((x * cnt) / y)
        tmp = tmp2 - tmp1 + 1

        answer -= tmp * k
        cnt += 1

    return answer