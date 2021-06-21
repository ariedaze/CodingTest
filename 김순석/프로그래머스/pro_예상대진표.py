def solution(n, a, b):
    answer = 0
    a, b = min(a, b), max(a, b)
    exp = 1
    tmp = b

    while tmp > 2:
        tmp //= 2
        exp += 1
    s = 1
    e = 2 ** exp
    print(e)
    while True:
        mid = (s + e) / 2
        if (mid - a) * (mid - b) < 0:
            answer = exp
            return answer
        else:
            exp -= 1
            if mid > b:
                e = int(mid)
            else:
                s = int(mid) + 1

    return answer

n, a, b = 16, 2, 8
print(solution(n, a, b))