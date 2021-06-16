# 첫번쨰 풀이 시간초과남
# def solution(s):
#     answer = -1
#     s_list = list(map(str,s))
#     #pop을 두번이나 써서 사실상 for문을 4개돌린것과 같기 때문 최대한 pop의 사용을 줄여야겠다.
#     while len(s_list) > 0:
#         for i in range(len(s_list)-1):
#             if s_list[i] == s_list[i + 1]:
#                 s_list.pop(i)
#                 s_list.pop(i)
#
#                 answer = 1
#                 break
#         else :
#             answer = 0
#             break
#
#     return answer

def solution(s):
    answer = -1
    s_list = []

    for c in s:
        # 만약 리스트에 하나도 없으면 가장 처음의 값은 넣어줘야한다.
        if len(s_list) == 0:
            s_list.append(c)
            continue

        if s_list[-1] == c:
            s_list.pop()

        else:
            s_list.append(c)

    if len(s_list) > 0:
        answer = 0
    else:
        answer = 1

    return answer

s = 'baabaa'
print(solution(s))