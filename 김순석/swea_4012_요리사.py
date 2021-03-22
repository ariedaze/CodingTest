from itertools import combinations

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr =[]
    num = [i for i in range(0, N)]
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    p = list(combinations(num, N // 2))
    l = len(p)
    min_val = 0xfffffff
    for i in range(l//2):
        sum_a = sum_b = 0
        A = list(combinations(p[i], 2))
        B = list(combinations(p[l-i-1], 2))

        for a in A:
            sum_a += arr[a[0]][a[1]] + arr[a[1]][a[0]]

        for b in B:
            sum_b += arr[b[0]][b[1]] + arr[b[1]][b[0]]

        if min_val > abs(sum_a - sum_b):
            min_val = abs(sum_a - sum_b)

        if min_val == 0:
            break
    print('#{} {}'.format(t, min_val))