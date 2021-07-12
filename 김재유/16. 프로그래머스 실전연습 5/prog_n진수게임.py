def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]


def solution(n, t, m, p):
    result = ""
    answer = ""
    num = 0
    while len(result) <= (t + 1) * m:
        result += convert(num, n)
        num += 1
    for i in range(t):
        answer += result[p - 1 + m * i]

    return answer