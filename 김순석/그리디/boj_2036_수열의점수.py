import sys
ln = sys.stdin.readline

N = int(ln())

minus = []
zero = False
one = []
plus = []
score = 0
for _ in range(N):
    n = int(ln())

    if n == 1:
        score += 1
        continue
    elif n == 0:
        zero = True
        continue

    elif n < 0:
        minus.append(n)
    elif n > 1:
        plus.append(n)

minus.sort()
plus.sort()
len_m = len(minus)
len_p = len(plus)

if len_m % 2 == 0:
    for i in range(0, len_m, 2):
        score += minus[i] * minus[i+1]


elif len_m % 2 == 1:
    if zero:
        minus.pop()
    else:
        score += minus.pop()
    for i in range(0, len_m - 1, 2):
        score += minus[i] * minus[i+1]

if len_p % 2 == 0:
    for i in range(len_p - 1, 0, -2):
        score += plus[i] * plus[i-1]

elif len_p % 2 == 1:
    score += plus.pop(0)
    for i in range(len_p - 2, 0, -2):
        score += plus[i] * plus[i-1]

print(score)