def solution(record):
    answer = []
    user = {}
    # user dict에 change나 Enter가 들어오면 저장을 시킨다.
    for message in record:
        #split은 안의 공백을 기준으로 값을 쪼개서 저장
        if (message.split(' ')[0] == 'Enter') or (message.split(' ')[0] == 'Change'):
            # 마지막에 출력만하면 되니까 들어온 값을 계속 바꿔가면서 저장한다.
            user[message.split(' ')[1]] = message.split(' ')[2]

    for message in record:
        if message.split(' ')[0] == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(user[message.split(' ')[1]]))
        elif message.split(' ')[0] == 'Leave':
            answer.append("{}님이 나갔습니다.".format(user[message.split(' ')[1]]))
        else:
            pass

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))