import sys
# from collections import deque

sys.stdin = open('input/boj_16953_A to B.txt', 'r')
In = sys.stdin.readline

a, b = map(int, In().split())
s = []


def calc(x, cnt):
    global ans

    if x > b:
        return
    if x == b and cnt < ans:
        ans = cnt
        return ans
    calc(x * 10 + 1, cnt + 1)
    calc(x * 2, cnt + 1)
    return -1

ans = 0xfffff
calc(a, 1)
if ans != 0xfffff:
    print(ans)
else:
    print(-1)
