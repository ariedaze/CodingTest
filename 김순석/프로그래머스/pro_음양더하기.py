def solution(absolutes, signs):
    answer = 0
    for val, i in zip(absolutes, signs):
        # print(val, i)
        if i == False:
            answer -= val
        else:
            answer += val
    return answer