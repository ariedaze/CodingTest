def solution(lottos, win_nums):
    answer = []
    zero_cnt = 0
    num_cnt = 0
    for lotto in lottos:
        if lotto == 0:
            zero_cnt += 1
            continue
        if lotto in win_nums:
            num_cnt += 1

    if num_cnt >= 2:
        min_val = 7 - num_cnt
    else:
        min_val = 6

    if num_cnt + zero_cnt >= 2:
        max_val = 7 - (num_cnt + zero_cnt)
    else:
        max_val = 6
    answer = [max_val, min_val]
    return answer