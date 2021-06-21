def solution(info, query):
    answer = []
    string = []
    user_info = []
    user_dict = {}
    for q in query:
        tmp = q.split(' ')
        tmp_string = []
        for i in tmp:
            if i != 'and':
                tmp_string.append(i)
        string.append(tmp_string)

    for s in info:
        if str(s.split(' ')[:-1]) not in user_dict:
            user_dict[str(s.split(' ')[:-1])] = [s.split(' ')[-1]]

        else:
            user_dict.get(str(s.split(' ')[:-1])).append(s.split(' ')[-1])

    for i in range(len(string)):
        cnt = 0
        # print(string[i])
        for u in user_dict:
            # print(user_dict.get(u))
            if str(string[i][:-1]) == u:
                # print('같ㅌ다')
                for j in range(len(user_dict.get(u))):
                    # print(u.value())
                    # print(string[i][-1], u[j])
                    if int(string[i][-1]) > int(user_dict.get(u)[j]):
                        print('hi')
                        continue
                    for k in range(4):
                        if string[i][k] == '-':
                            continue
                        if string[i][k] != user_info[j][k]:
                            break
                    else:
                        cnt += 1
        answer.append(cnt)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

solution(info, query)
# def solution(info, query):
#     answer = []
#     string = []
#     user_info = []
#
#     for q in query:
#         tmp = q.split(' ')
#         tmp_string = []
#         for i in tmp:
#             if i != 'and':
#                 tmp_string.append(i)
#         string.append(tmp_string)
#
#     for s in info:
#         user_info.append(s.split(' '))
#     for i in range(len(string)):
#         cnt = 0
#         for j in range(len(user_info)):
#             if int(string[i][-1]) > int(user_info[j][-1]):
#                 continue
#             for k in range(4):
#                 if string[i][k] == '-':
#                     continue
#                 if string[i][k] != user_info[j][k]:
#                     break
#             else:
#                 cnt += 1
#         answer.append(cnt)
#
#     return answer