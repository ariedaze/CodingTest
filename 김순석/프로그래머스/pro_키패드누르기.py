dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(numbers, hand):
    answer = ''
    L, R = (3, 0), (3, 2)

    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            L = (numbers[i] // 3, 0)
            answer += 'L'

        if numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            R = ((numbers[i] // 3) - 1, 2)
            answer += 'R'

        if numbers[i] == 2 or numbers[i] == 5 or numbers[i] == 8:
            target = (numbers[i] // 3, 1)
            ans, l, r = calc(L, R, target, hand)
            answer += ans
            L, R = l, r

        if numbers[i] == 0:
            target = (3, 1)
            ans, l, r = calc(L, R, target, hand)
            answer += ans
            L, R = l, r
    return answer


def calc(l, r, t, hand):
    xl, yl, xr, yr = l[0], l[1], r[0], r[1]
    tx, ty = t[0], t[1]

    l_dist = abs(tx - xl) + abs(ty - yl)
    r_dist = abs(tx - xr) + abs(ty - yr)

    if l_dist == r_dist:

        if hand == 'left':
            l = t
            return 'L', l, r
        else:
            r = t
            return 'R', l, r

    if l_dist > r_dist:
        r = t
        return 'R', l, r
    if l_dist < r_dist:
        l = t
        return 'L', l, r

    return

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers, hand))
print()