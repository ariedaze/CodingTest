def solution(n, lost, reserve):
    new_lost = set(lost)
    new_reserve = set(reserve)
    for l in lost:
        for r in reserve:
            if l == r:
                new_lost.remove(l)
                new_reserve.remove(r)

    answer = n - len(new_lost)
    visited = [0] * (n + 1)

    for litem in new_lost:
        for ritem in new_reserve:
            if litem == ritem - 1 or litem == ritem + 1 and not visited[ritem]:
                visited[ritem] = 1
                answer += 1
                break

    return answer

n = 5
lost = [2,4]
reserve = [3]

solution(n, lost, reserve)