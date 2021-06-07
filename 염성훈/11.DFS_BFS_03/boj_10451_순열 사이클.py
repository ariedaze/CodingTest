import sys
sys.stdin = open("input.txt","r")

#dfs 수행 문제라고 보면된다.
def dfs(x):
    visited[x] = 1
    next = arr[x] #다음 방문 장소
    if not visited[next]: #방문 안했으면
        dfs(next)


t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int,input().split()))
    visited = [0] * (n + 1)
    answer = 0

    # 1부터 주어진 수까지 반복
    for i in range(1, n + 1):
        # 만약 방문안한 곳이 있다면 dfs수행
        if not visited[i]:
            dfs(i)
            answer += 1

    print(answer)
