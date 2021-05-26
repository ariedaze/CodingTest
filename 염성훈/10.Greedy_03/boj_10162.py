import sys
sys.stdin = open("input.txt","r")

n = int(input())
a, b, c = 0, 0, 0
flag = True

while n:
    if n % 10 != 0:
        flag = False
        break
    if n >= 300:
        a += n//300
        n %= 300
    elif n >= 60:
        b += n//60
        n %= 60
    else:
        c += n//10
        n %= 10
if flag:
    print(a, b, c)
else:
    print(-1)
