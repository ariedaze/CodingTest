s = 'cdcd'

from collections import deque

def solution(s):
    s = deque(s)
    check = deque()
    while s:
        char = s.popleft()
        if check:
            if check[-1] == char:
                check.pop()
            else:
                check.append(char)
        else:
            check.append(char)
    if check:
        return 0
    else:
        return 1

print(solution(s))
