N, K, M = map(int, input().split())
# print(N)
pivot = K
tmp = 1
cnt = 1
for i in range(1, N + 1):
    pivot = (tmp + K - 1) % N
    if pivot == 0:
        pivot = N
    if pivot == M:
        break
    elif pivot < M:
        M -= 1
    cnt += 1
    tmp = pivot
    N -= 1

print(cnt)
