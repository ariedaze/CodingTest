def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        tmp = ''
        for i in range(len(tree)):
            if tree[i] in skill:
                tmp += tree[i]
        for i in range(len(tmp)):
            if skill[i] != tmp[i]:
                break
        else:
            answer += 1
    return answer