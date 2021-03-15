import sys
# sys.stdin = open('input/boj_2231_분해합.txt', 'r')
In = sys.stdin.readline

N = int(In())
n = len(str(N))
ans = 0

if n >= 3:
    s = N - (9 * n)
    for i in range(s, N):
        calc = '+'.join(str(i))
        k = eval(calc)
        if i + k == N:
            ans = i
            break
else:
    for i in range(1, N):
        calc = '+'.join(str(i))
        k = eval(calc)
        if i + k == N:
            ans = i
            break

print(ans)