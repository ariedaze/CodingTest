def solution(n):
    result = 1
    sum_list = [0]
    for i in range(1, n//2+2):
        num = sum_list[-1]+i
        sum_list.append(num)
        if num < n:
            start = i
    start += 1
    for num in range(start, len(sum_list)):
        for check in range(num):
            now_num = sum_list[num] - sum_list[check]
            if now_num == n:
                result += 1
                break
            elif now_num < n:
                break
    return result