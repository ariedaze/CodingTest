def solution(s):
    answer = []
    s = s[2:-2]
    divs = s.split('},{')
    divs.sort(key=len)
    for c in divs:
        c_list = c.split(',')
        for i in c_list:
            #i가 answer에 없으면 하나씩 추가해주면된다. 집함의 크기가 가장 작은거부터
            #검색되니까 튜플대로 나오게됨.
            if int(i) not in answer:
                answer.append(int(i))

    return answer

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
solution(s)