def solution(new_id):
    answer = ''
    target = ['.', '-', '_']
    l = len(new_id)
    new_id = new_id.lower()
    temp1 = ''
    for i in range(l):
        if new_id[i].isalnum():
            temp1 += new_id[i]
        elif new_id[i] in target:
            temp1 += new_id[i]

    temp2 = ''
    pivot = 0
    for i in range(len(temp1)):
        i += pivot
        if i <= len(temp1) - 1:
            if temp1[i] != '.':
                temp2 += temp1[i]

            else:
                for j in range(i+1, l):
                    if j >= len(temp1):
                        break
                    if temp1[i] == temp1[j]:
                        continue
                    elif temp1[i] != temp1[j]:
                        temp2 += temp1[i]
                        pivot += j - i - 1
                        break


    answer = temp2
    if len(answer) != 0 and answer[0] == '.':
        answer = answer[1:]
    if len(answer) != 0 and answer[-1] == '.':
        answer = answer[:-1]
    if len(answer) == 0:
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[0:15]
    if answer[-1] == '.':
        answer = answer[:-1]

    while len(answer) <= 2:
        answer += answer[-1]
    return answer