def solution(name):
    answer = 0
    N = len(name)
    loc = []
    cnt = 0
    ans = 0

    # A가 아닌 알파벳의 인덱스를 loc에 저장
    for i in range(N):
        if name[i] != 'A':
            loc.append(i)
    # loc 비었으면(A로만 이루어진경우) 0 반환
    if not loc:
        return 0

    elif len(loc) == 1:
        if loc[0] <= N // 2:
            ans = loc[0]
        else:
            ans = N - loc[0]

    # 바꿔야할 알파벳 개수가 2 이상이면
    else:
        for i in range(len(loc) - 1):
            ans = min(loc[-1], loc[i] * 2 + len(name[loc[i + 1]:]))


    # 조작할 문자들의 조작 횟수
    for i in loc:
        # 알파벳 순 N 이전의 것이면 A만큼 빼주고
        if ord(name[i]) <= ord('N'):
            answer += ord(name[i]) - ord('A')
        # 아닌 경우(이전 알파벳으로 이동하는 경우)
        else:
            answer += 91 - ord(name[i])
    return answer + ans