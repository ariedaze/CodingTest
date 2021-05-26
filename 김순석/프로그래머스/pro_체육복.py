def solution(n, lost, reserve):
    answer = 0
    reserve.sort()
    lost.sort()
    new_reserve = []
    new_lost = []
    for i in range(len(reserve)):
        for j in range(len(lost)):
            if reserve[i] == lost[j]:
                lost[j] = 0
                reserve[i] = 0
                break
    for i in reserve:
        if i != 0:
            new_reserve.append(i)
    for i in lost:
        if i != 0:
            new_lost.append(i)

    for i in range(len(new_reserve)):
        for j in range(len(new_lost)):
            if new_reserve[i] - 1 == new_lost[j] and new_lost[j] != 0:
                new_lost[j] = -1
                break
            elif new_reserve[i] + 1 == new_lost[j] and new_lost[j] != 0:
                new_lost[j] = -1
                break

    cnt = len(new_lost) - new_lost.count(-1)
    answer = n - cnt
    return answer