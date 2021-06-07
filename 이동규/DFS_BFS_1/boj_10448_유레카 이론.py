import sys
sys.stdin = open('input/boj_10448_유레카 이론.txt', 'r')

from collections import deque

def dfs():
    stack = deque()
    stack.append([3, 2, 2, 2])

    while stack:
        sum_tmp, a, b, c = stack.pop()

        for i in range(3):
            if i == 0 and sum_tmp+a <= N:
                if sum_tmp+a == N:
                    return 1
                visit[sum_tmp + a] = 1
                stack.append([sum_tmp+a, a+1, b, c])
            elif i == 1 and sum_tmp+b <= N:
                if sum_tmp+b == N:
                    return 1
                visit[sum_tmp + b] = 1
                stack.append([sum_tmp+b, a, b+1, c])
            elif i == 2 and sum_tmp+c <= N:
                if sum_tmp+c == N:
                    return 1
                visit[sum_tmp + c] = 1
                stack.append([sum_tmp+c, a, b, c+1])
    return 0


for T in range(int(input())):
    N = int(input())
    sum = 0
    result = 0
    visit = [0 for _ in range(1001)]
    visit[3] = 1
    if N == 3:
        print(1)
    else:
        print(dfs())
