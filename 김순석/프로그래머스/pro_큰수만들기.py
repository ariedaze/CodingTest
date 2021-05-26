def solution(number, k):
    answer = ''
    tmp = []
    for num in number:
        while tmp and tmp[-1] < num and k > 0:
            tmp.pop()
            k -= 1
        tmp.append(num)

    while k > 0:
        tmp.pop()
        k = -1
    # print(''.join(tmp))
    answer = ''.join(tmp)
    return answer