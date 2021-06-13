import sys
ln = sys.stdin.readline

T = int(ln())
for t in range(1, T + 1):
    N = int(ln())
    num = [0] + list(map(int, ln().split()))
    visit = [0] * (N + 1)
    pivot = 0
    ans = 0
    for i in range(1, N+1):
        pivot = i
        if visit[pivot] == 0:
            while visit[pivot] == 0:
                visit[pivot] = 1
                pivot = num[pivot]
            ans += 1

    print(ans)