import sys
In = sys.stdin.readline

T= int(In())
for t in range(1, T + 1):
    n = int(In())

    d = [0] * 11
    d[1] = 1
    d[2] = 2
    d[3] = 4
    for i in range(4, n + 1):
        d[i] = d[i - 1] + d[i -2] + d[i - 3]
    print(d[n])