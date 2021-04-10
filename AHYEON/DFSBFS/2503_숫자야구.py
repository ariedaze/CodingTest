N = int(input())
answer_list = [str(x) for x in range(123, 988) if not '0' in str(x) and len(set(str(x))) == 3]


for _ in range(N):  # 질문, s, b
    q, s, b = map(int, input().split())
    question = str(q)

    for ans in answer_list[:]:
        check_s, check_b = 0, 0
        for i in range(3):
            if ans[i] == question[i]:
                check_s += 1
            elif ans[i] in question:
                check_b += 1

        if check_b != b or check_s != s:
            answer_list.remove(ans)

print(len(answer_list))