def solution(n):
    answer = ''
    while n > 0:
        n, rest = divmod(n, 3)
        answer = "412"[rest] + answer
        if not rest:
            n -= 1

    return answer

n = 6
solution(n)