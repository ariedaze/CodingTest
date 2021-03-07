import sys; sys.stdin = open('input_data/2217.txt')

rope_num = int(input())
ropes = []
for _ in range(rope_num):
    ropes.append(int(input()))
ropes.sort(reverse=True)
max_weight = 0
for i in range(rope_num):
    can_weight = (i+1) * ropes[i]
    if max_weight < can_weight:
        max_weight = can_weight
print(max_weight)

