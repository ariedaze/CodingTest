def solution(s):
    answer = 1000000

    for slice in range(1, len(s)//2 + 2):
        res = ''
        # 글자 앞에 나타나는 수를 cnt로 나타낸다.
        cnt = 1
        tmp = s[:slice]
        # 배수로 끊어서 나타냄.
        for i in range(slice, len(s)+ slice, slice):
            if tmp == s[i:i+slice]:
                cnt += 1
            else:
                # cnt가 1 이면 temp를 그대로 res에 더해준다.
                if cnt == 1:
                    res += tmp
                # 지금까지 cnt된 값을 더해 res에 담아 tmp와 함꼐 넣어준다.
                else:
                    res = res + str(cnt) + tmp
                tmp = s[i:i+slice]
                cnt = 1

        answer = min(answer, len(res))
    return answer

s = "aabbaccc"
print(solution(s))