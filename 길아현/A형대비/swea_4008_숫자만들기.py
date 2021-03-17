# import sys
# sys.stdin = open('input/swea_4008_숫자만들기.txt', 'r')


def calc(a, b, op):
    if op == 0:
        return a + b
    elif op == 1:
        return a - b
    elif op == 2:
        return a * b
    elif op == 3:
        return int(a / b)


def dfs(depth, candi):
    global max_ans, min_ans
    if depth == N-1:
        max_ans = max(max_ans, candi)
        min_ans = min(min_ans, candi)
        return
    for i in range(4):
        if operator[i]:
            operator[i] -= 1
            dfs(depth+1, calc(candi, number[depth+1], i))
            operator[i] += 1


for tc in range(1, int(input())+1):
    N = int(input())
    operator = list(map(int, input().split())) # + - * /
    number = list(map(int, input().split()))
    max_ans = -100000000
    min_ans = 100000000
    dfs(0, number[0])
    print(f'#{tc} {max_ans-min_ans}')
