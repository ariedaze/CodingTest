import sys
ln = sys.stdin.readline

N = int(ln())
d = [0] * (N + 2)
max_val = 0

for i in range(1, N + 1):
    T, P = map(int, ln().split())

    if d[i] > max_val:
        max_val = d[i]

    if i + T > N + 1:
        continue

    d[i + T] = max(max_val + P, d[i + T])

print(max(d))