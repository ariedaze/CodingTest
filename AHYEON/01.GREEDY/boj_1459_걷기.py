x, y, w, s = map(int, input().split())
x, y = min(x, y), max(x, y)


# 가로세로만 / 가로세로 + 평행선 / 평행선만
print(min((x+y)*w, x*s + (y-x)*w, (y - (y+x)%2)*s + (y+x)%2*w))
