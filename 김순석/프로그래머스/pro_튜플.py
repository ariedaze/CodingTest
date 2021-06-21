def solution(s):
    answer = []
    string = []
    tmp_string = []
    for i in range(1, len(s) - 1):
        if s[i] == '{':
            pivot = i
        if s[i] == '}':
            tmp = ''
            for j in range(pivot, i+1):
                if s[j].isnumeric():
                    tmp += s[j]
                elif not s[j].isnumeric() and tmp != '':
                    string.append(int(tmp))
                    tmp = ''
            tmp_string.append(string)
            string = []
    tmp_string.sort(key=len)
    for i in tmp_string:
        for j in range(len(i)):
            if i[j] not in answer:

                answer.append(i[j])
    return answer

# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))