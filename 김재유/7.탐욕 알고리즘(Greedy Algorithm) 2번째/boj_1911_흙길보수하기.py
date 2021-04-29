#TODO 파트7

import sys; sys.stdin = open('input_data/1911.txt')

hole, length = map(int, input().split())
hole_list = []
for _ in range(hole):
    hole_list.append(list(map(int,input().split())))
hole_list.sort()
result = 0
now = 0
for i in range(hole):
    now_hole = hole_list[i]
    if now < now_hole[0]:
        now = now_hole[0]
    target = now_hole[1]
    if now < target:
        if (target-now)%length:
            result += (target-now)//length + 1
            now += ((target-now)//length +1)* length
        else:
            result += (target - now) // length
            now += ((target - now) // length ) * length
print(result)


