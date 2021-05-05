#TODO 파트7 시간초과

import sys; sys.stdin = open('input_data/10800.txt')
num = int(input())
ball_list = [list(map(int, sys.stdin.readline().split())) for _ in range(num)]
for ball1 in ball_list:
    eating = 0
    for ball2 in ball_list:
        if ball1[0] == ball2[0]: continue
        if ball1[1] <= ball2[1]: continue
        eating += ball2[1]
    print(eating)