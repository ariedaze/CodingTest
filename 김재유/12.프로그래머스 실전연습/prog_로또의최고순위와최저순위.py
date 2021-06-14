def solution(lottos, win_nums):
    joker = 0
    hit = 0
    for lotto in lottos:
        if not lotto:
            joker +=1
        if lotto in win_nums:
            hit += 1
    min_score = min(7-hit, 6)
    max_score = min(7-(hit+joker), 6)
    return [max_score, min_score]