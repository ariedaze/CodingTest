N, K = map(int, input().split())


def func(n, k):
    dict = {}
    for i in range(1, n + 1):
        dict[i] = 1

    target = 1
    cnt = 0
    rot = 0

    while True:
        if dict[target] == 1 and rot == k - 1:
            dict[target] = 0
            cnt += 1
            rot = 0
        elif dict[target] == 0:
            target += 1
            if target > n:
                target -= n
        else:
            rot += 1
            target += 1
            if target > n:
                target -= n

        if cnt == (n - k + 1):
            break

    x = []
    for i in range(1, n + 1):
        if dict[i] == 1:
            x.append(i)
    return x[-1]


print(func(N, K))

