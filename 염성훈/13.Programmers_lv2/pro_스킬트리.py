def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        match = []
        for alpha in skill_tree:
            if alpha in skill:
                match.append(alpha)

        for i in range(len(match)):
            if match[i] != skill[i]:
                break
        else:
            answer += 1

    return answer

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
solution(skill, skill_trees)