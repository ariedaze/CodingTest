TC = int(input())


def dfs(n, part):
    global ans
    if part == n:
        ans += 1
        return
    elif part > n:
        return
    for i in range(1, 4):
        dfs(n, part+i)


for _ in range(TC):
    n = int(input())
    ans = 0
    dfs(n, 0)
    print(ans)