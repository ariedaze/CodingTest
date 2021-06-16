def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        result = True
        check = ''
        for char in skill_tree:
            if char in skill:
                check += char
                if not skill.startswith(check):
                    result = False
        if result:
            answer += 1
    return answer