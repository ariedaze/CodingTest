import sys; sys.stdin = open('input_data/12851.txt')
from collections import deque

now, target = map(int, input().split())
fast = abs(target-now)
result = 0
Q = deque()
Q.append([now, 0])
visit = [0] * 100001
while Q:
    number, depth = Q.popleft()
    if visit[number]:
        if visit[number] < depth:
            continue
        else:
            visit[number] = depth
    else:
        visit[number] = depth

    if target == number:
        if fast > depth:
            fast = depth
            result = 1
        elif fast == depth:
            result += 1
    else:
        if depth + 1 <= fast:
            if number*2 < 100001:
                Q.append([number*2, depth+1])
            if number < 100000:
                Q.append([number+1, depth+1])
            if number > 0:
                Q.append([number-1, depth+1])
print(fast)
print(result)
