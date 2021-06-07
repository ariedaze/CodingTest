import sys
sys.stdin = open('input/boj_9205_맥주 마시면서 걸어가기.txt', 'r')

from collections import deque

def calculate_distance(s, g):
    return abs(s[0] - g[0]) + abs(s[1] - g[1])


def dfs(index):
    global flag

    queue = deque()
    queue.append(index)

    while queue:
        idx = queue.popleft()

        if calculate_distance(idx, GOAL) <= 1000:
            print('happy')
            flag = 1
            return

        for i, v in enumerate(CU):
            if calculate_distance(idx, v) <= 1000 and visit[i] == False:
                visit[i] = True
                queue.append(v)

    print('sad')


    #
    # if flag:
    #     return
    #
    # if calculate_distance(index, GOAL) <= 1000:
    #     print('happy')
    #     flag = 1
    #     return
    #
    # for idx, v in enumerate(CU):
    #     if calculate_distance(index, v) <= 1000 and visit[idx] == False:
    #         visit[idx] = True
    #         dfs(v)
    #         visit[idx] = False


for _ in range(int(input())):
    N = int(input()) # 편의점의 수
    START = list(map(int, input().split()))
    CU = [list(map(int, input().split())) for _ in range(N)]
    GOAL = list(map(int, input().split()))
    flag = 0
    visit = [False for _ in range(N)]

    dfs(START)