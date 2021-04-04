import sys
ln = sys.stdin.readline

N = int(ln())

num = [1, 5, 10, 50]
# chk = [0] * (N + 1)
lst = []
for i in range(N + 1):
    for j in range(N + 1 - i):
        for k in range(N + 1 - i - j):
            l = N - i - j - k
            calc = i + (5 * j) + (10 * k) + (50 * l)
            lst.append(calc)
print(len(set(lst)))