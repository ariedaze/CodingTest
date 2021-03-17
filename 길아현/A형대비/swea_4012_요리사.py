# import sys
# sys.stdin = open('input/swea_4012_요리사.txt', 'r')


def maat(food):
    s = 0
    for i in range(N//2):
        for j in range(i+1, N//2):
            s += graph[food[i]][food[j]] + graph[food[j]][food[i]]
    return s


def dfs(idx, j):
    global ans
    if idx == N // 2:
        A = []
        B = []
        for i in range(N):
            if visited[i]:
                A.append(i)
            else:
                B.append(i)
        a = maat(A)
        b = maat(B)
        ans = min(ans, abs(a-b))

    for i in range(j, N):
        if not visited[i]:
            visited[i] = 1
            dfs(idx+1, i+1)
            visited[i] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    ans = 200000
    dfs(0, 0)

    print(f'#{tc} {ans}')