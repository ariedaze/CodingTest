def solution(s):
    answer = 0
    dic = {
        '{' : '}',
        '[' : ']',
        '(' : ')'
    }

    for i in range(len(s)):
        right = list(s[i:] + s[:i])
        left = []
        while right:
            temp = right.pop(0)
            if not left:
                left.append(temp)
            else:
            # left에 들어있는 값이 닫힌 괄호면 어떤괄호가 들어와도 조건만족 X
                if left[-1] in ['}', ']', ')']:
                    break
                # 열린괄호이고 right의 첫번째 값에서 뽑은 값이 닫힌 괄호라면
                # left 리스트의 값을 뽑아준다.
                if dic[left[-1]] == temp:
                    left.pop()
                #열린괄호지만 들어온 값과 매칭이 안될경우 뽑은 temp를 그대로 넣어준다.
                else:
                    left.append(temp)

        if not left:
            answer += 1

    return answer

s = "[](){}"
solution(s)
