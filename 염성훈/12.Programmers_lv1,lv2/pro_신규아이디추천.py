def solution(new_id):
    new_id = new_id.lower()

    answer = ''
    for item in new_id:
        if item.isalnum() or item in '-_.':
            answer += item

    while '..' in answer:
        answer = answer.replace('..', '.')

    if answer[0] == '.':
        answer = answer[1:]

    if len(answer) > 0:
        if answer[-1] == '.':
            answer = answer[:len(answer) - 1]

    if answer == '':
        answer = 'a'

    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:len(answer) - 1]

    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    return answer