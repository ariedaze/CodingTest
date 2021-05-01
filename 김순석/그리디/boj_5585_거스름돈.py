import sys
ln = sys.stdin.readline

N = int(ln())
n = 1000 - N
cnt = 0

while n > 0:
    if n >= 500:
        cnt += 1
        n -= 500
        continue

    elif n >= 100:
        cnt += 1
        n -= 100
        continue

    elif n >= 50:
        cnt += 1
        n -= 50

    elif n >= 10:
        cnt += 1
        n -= 10
        continue

    elif n >= 5:
        cnt += 1
        n -= 5
        continue

    elif n >= 1:
        cnt += 1
        n -= 1

print(cnt)