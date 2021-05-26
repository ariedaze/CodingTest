from collections import deque

people = [70, 80, 50]
limit = 100

people.sort()
Q = deque(people)
total = 0
while Q:
    boat = Q.pop()
    while boat < limit:
        if Q:
            light = Q.popleft()
            if boat + light <= limit:
                boat += light
            else:
                Q.appendleft(light)
                break
        else:
            break
    total += 1
print(total)
