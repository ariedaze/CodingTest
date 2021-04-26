def solution(s):
    s_len = len(s)  # 아무리 커봐야 입력되는 문자열 크기
    answer = s_len

    # input 1000 이하 => 완전탐색
    for interval in range(1, int(s_len/2) + 1):
        pos = 0  # 연산 수행하는 위치

        candi_answer = s_len

        while pos + interval <= s_len:
            unit = s[pos:pos+interval]
            pos += interval

            cnt = 0
            while pos + interval <= s_len:
                if unit == s[pos:pos+interval]:
                    cnt += 1
                    pos += interval
                else:
                    break
            if cnt > 0: # 반복된게 있었다?!
                candi_answer -= (cnt * interval)

                if cnt < 9: candi_answer += 1
                elif cnt < 99: candi_answer += 2
                elif cnt < 999: candi_answer += 3
                else: candi_answer += 4

        answer = min(answer, candi_answer)

    return answer

print(solution('aaaaaa'))