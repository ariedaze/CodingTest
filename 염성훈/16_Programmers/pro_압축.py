def solution(msg):
    # 색인 값을 저장하기위해 dict()를 사용한다.
    table = dict()
    for idx, value in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1):
        table[value] = idx
        last_idx = idx
    idx = 1
    answer = []
    letter = msg[0]
    
    while idx < len(msg):
        # 현재 입력 + 다음 글자 조합이 색인에 없는 경우 현재
        if letter + msg[idx] not in table:
            #현재 입력을 배열에 저장하고
            answer.append(table[letter])
            #새 단어를 dict에 저장한다.
            last_idx += 1
            table[letter + msg[idx]] = last_idx
            #그리고 현재의 입력값에 다음 단어를 넣는다.
            letter = msg[idx]
            idx += 1
            continue
        #이미 dict에 저장 되어 있으면 다음 단어를 현재 입력에 추가한다.
        letter += msg[idx]
        idx += 1
    
    answer.append(table[letter])
        
    return answer
