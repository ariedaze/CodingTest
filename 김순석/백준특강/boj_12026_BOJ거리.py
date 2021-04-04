import sys
ln = sys.stdin.readline

N = int(ln())
block = ln().rstrip()
d = [0xffffffff] * N


def get_prev(x):
    if x == "B":
        return "J"
    elif x == "O":
        return "B"
    elif x == "J":
        return "O"


d[0] = 0
for i in range(1, N):
    prev = get_prev(block[i])
    for j in range(i):
        if block[j] == prev:
            d[i] = min(d[i], d[j] + pow(i - j, 2))

print(d[N - 1] if d[N - 1] != 0xffffffff else -1)
