import sys

ln = sys.stdin.readline

X, Y, W, S = map(int, ln().split())
X, Y = min(X, Y), max(X, Y)

# 2w < s
temp1 = (X + Y) * W

# 2w > s
# i) 대각선 최소한으로 쓰는경우
temp2 = X * S + (Y - X) * W

# ii) 대각선 많이쓰는경우
r = (X + Y) % 2

temp3 = (r * W) + (Y - r) * S


print(min(temp1, temp2, temp3))