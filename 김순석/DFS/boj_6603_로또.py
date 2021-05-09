import sys
ln = sys.stdin.readline


def dfs(v, depth):
    if depth == 6:
        for i in range(k):
            if tmp[i]:
                print(lst[i], end=' ')
        print()
        return

    for i in range(v, k):
        tmp[i] = 1
        dfs(i + 1, depth + 1)
        tmp[i] = 0


while True:

    cnt = 0
    lst = list(map(int, ln().split()))
    if lst[0] == 0:
        break

    k = lst[0]
    lst.pop(0)
    tmp = [0 for _ in range(k)]
    dfs(0, 0)
    print()

