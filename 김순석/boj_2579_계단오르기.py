import sys
inp = sys.stdin.readline

n = int(inp())
arr = [0]
d = [[0, 0] for _ in range(n + 1)]

for _ in range(n):
    arr.append(int(inp()))

d[1] = [arr[1], 0]

for i in range(2, n + 1):
    d[i][0] = max(d[i - 2]) + arr[i]
    d[i][1] = d[i-1][0] + arr[i]
print(max(d[n]))
