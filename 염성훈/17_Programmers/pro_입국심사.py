def solution(n, times):
    left = 1
    #최악의 시간대를 선정한다. 가장 큰 곳에 다갔을 경우
    right = n * max(times)


    while left < right:
        mid = (left + right) // 2
        total = 0
    
        for t in times:
            total += mid // t
        print(total)

        if total >= n:
            right = mid
        else:
            left = mid + 1

    answer = left
    print(answer)

    return answer

n = 6
times = [7, 10]
solution(n, times)