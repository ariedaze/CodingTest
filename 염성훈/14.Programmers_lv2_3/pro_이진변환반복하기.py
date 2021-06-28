def solution(s):
    answer = [0, 0]
    cnt = 0
    zero = 0

    while True:
        if s == "1":
            break
        else:
            zero += s.count('0')
            s = format(len(s.replace("0","")),"b")
            cnt += 1
    answer[0] = cnt
    answer[1] = zero

    return answer

s = "110010101001"
solution(s)