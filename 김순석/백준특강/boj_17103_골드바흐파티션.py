import sys
ln = sys.stdin.readline

T = int(ln())
lst = [int(ln()) for _ in range(T)]
max_val = max(lst)

prime = [False, False] + [True] * (max_val - 1)

# 1 2 4 8 16

for i in range(2, int(max_val ** 0.5) + 1):
    if prime[i]:
        for j in range(i + i, max_val + 1, i):
            # if prime[j]:
            prime[j] = False

# print(prime)
for n in lst:
    cnt = 0
    for i in range((n // 2) + 1):
        if prime[i] and prime[n - i]:
            cnt += 1
    print(cnt)
