import sys
sys.stdin = open('input/boj_10451_순열 사이클.txt', 'r')

from collections import deque

def dfs(idx):
    stack = deque()
    stack.append(idx)

    while stack:
        S, G = stack.pop()

        if visit[G] == False:
            visit[G] = True
            stack.append(ADJ_LIST[G-1])


for _ in range(int(input())):
    N = int(input()) # 정점의 수
    GOAL = list(map(int, input().split()))
    ADJ_LIST = list(zip([ i for i in range(1, N+1)], GOAL))
    visit = [False for _ in range(N + 1)]
    result = 0

    for s, g in ADJ_LIST:
        if visit[s] == False:
            result += 1
            dfs([s, g])

    print(result)
