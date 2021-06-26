def solution(new_id):
    new_id = new_id.lower() # 1

    answer = ''
    for i in new_id:  # 2
        if i.isalnum() or i in '-_.':
            answer += i

    while '..' in answer:
        answer = answer.replace('..', '.')

    if answer and answer[0] == '.':  # 4
        answer = answer[1:]

    if answer and answer[-1] == '.':
        answer = answer[:-1]

    if not answer:  # 5
        answer = 'a'

    if len(answer) >= 16:  # 6
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    while len(answer) <= 2:
        answer += answer[-1]

    return answer