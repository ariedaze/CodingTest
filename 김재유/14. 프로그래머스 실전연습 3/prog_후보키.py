from itertools import combinations

def solution(relation):
    result = []
    cols = len(relation[0])
    students = len(relation)
    possibles = []
    for i in range(1, cols+1):
        possibles.extend(map(set,combinations(range(cols), i)))
    for possible in possibles:
        already = []
        for i in range(students):
            now = [relation[i][j] for j in possible]
            if now in already:
                break
            already.append(now)
        else:
            result.append(possible)
    answer = [1]*len(result)
    for i in range(len(result)):
        if not answer[i]:
            continue
        for j in range(i+1, len(result)):
            if not answer[j]:
                continue
            if result[i] < result[j]:
                answer[j] = 0

    return sum(answer)