import math

N, M, K = map(int, input().split())

if N % 2 != 0:
    N -= 1
    K -= 1

if N >= (M * 2):
    intern = N - (M * 2)
    if K - intern > 0:
        cnt = math.ceil((K - intern) / 3)
        result = M - cnt
    else:
        result = M

else:
    intern = M - (N // 2)
    if K - intern > 0:
        cnt = math.ceil((K - intern) / 3)
        result = (N // 2) - cnt
    else:
        result = (N // 2)


if result < 0:
    result = 0

print(result)