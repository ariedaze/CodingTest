from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            comb = combinations(sorted(order), c)
            temp += comb

        cnt = Counter(temp)

        if len(cnt) != 0 and max(cnt.values()) != 1:
            for i in cnt:
                if cnt[i] == max(cnt.values()):
                    answer.append(''.join(i))

    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))