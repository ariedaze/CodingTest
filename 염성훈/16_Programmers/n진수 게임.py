def solution(n, t, m, p):
    answer = ''
    num = list()
    j = 0
    # 참가 인원이 m명인 사람들에게 t개씩 말하는 경우를 모두 저장
    while len(num) <= (t * m):
        # extend는 각 항목을 분리해서 num에 넣어주게 된다.
        num.extend(convert(j, n))
        j += 1
    idx = p - 1
    for i in range(0, t):
        answer += num[idx + (i * m)]
    return answer


def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base)

    if q == 0:
        return temp[r]
    else:
        return convert(q, base) + temp[r]