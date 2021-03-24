import sys
inp = sys.stdin.readline

n = int(inp())
arr = [0]
d = [0] * (n + 1)
for _ in range(n):
    arr.append(int(inp()))

# d[1] = arr[1]
# d[2] = arr[1] + arr[2]
d[3] = max(arr[1], arr[2]) + arr[3]
d[4] = max(arr[1] + arr[2], arr[1] + arr[3]) + arr[4]
# print(arr)
for i in range(5, n + 1):
    d[i] = max(d[i - 3] + d[i - 2], d[i - 3] + d[i - 1]) + arr[i]
print(d[n])