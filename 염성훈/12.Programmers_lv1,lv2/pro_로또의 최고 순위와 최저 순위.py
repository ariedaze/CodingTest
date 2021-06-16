def check_rank(num):
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    answer = []
    high = 0
    low = 0
    for lotto in lottos:
        if lotto in win_nums:
            low += 1
        if lotto == 0:
            high += 1
    high += low
    answer.append(check_rank(high))
    answer.append(check_rank(low))

    return answer