from itertools import combinations
from collections import defaultdict
import bisect


def solution(info, query):
    answer = []

    dict = defaultdict(list)

    for i in info:
        key = i.split()
        score = int(key.pop())
        keys = []
        dict[''.join(key)].append(score)

        for j in range(4):
            candi = list(combinations(key, j))
            for c in candi:
                dict[''.join(c)].append(score)

    for i in dict:
        dict[i].sort()

    for q in query:
        q = q.replace('and', '').replace('-', '')
        key = q.split()
        score = int(key.pop())
        key = ''.join(key)

        answer.append(len(dict[key])-bisect.bisect_left(dict[key], score))

    return answer