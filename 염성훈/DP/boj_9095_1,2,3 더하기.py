import sys
sys.stdin = open("input.txt", "r")

T = int(input())

d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4

for t in range(1,T + 1):
    N = int(input())

    for i in range(4, N + 1):
        d[i] = d[i - 3] + d[i - 2] + d[i - 1]

    print(d[N])