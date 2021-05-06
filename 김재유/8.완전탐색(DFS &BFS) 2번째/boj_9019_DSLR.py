import sys; sys.stdin = open('input_data/9019.txt')
from collections import deque

for t in range(int(input())):
    now, target = map(int, input().split())
    Q = deque()
    num_list = [0]*10000
    Q.append([now, ""])
    while Q:
        now, course = Q.popleft()
        if now == target:
            print(course)
            break
        if num_list[now] : continue
        num_list[now] = 1
        Q.append([(now*2)%10000, course+"D"])
        Q.append([now-1 if now > 0 else 9999, course+"S"])
        if now >= 1000:
            Q.append([(now%1000)*10 + now//1000, course + "L"])
            Q.append([now//10 + (now%10)*1000, course + "R"])
        elif now > 0:
            Q.append([now*10, course + "L"])
            Q.append([now//10 + (now%10)*1000, course + "R"])


