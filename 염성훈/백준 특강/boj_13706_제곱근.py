import sys
sys.stdin = open("input.txt","r")

N = int(input())

s, e = 1, N

while True:
    mid = (s + e) // 2

    mid_sqr = mid ** 2

    if mid_sqr == N:
        print(mid)
        break

    if mid_sqr > N:
        e = mid - 1
    else:
        s = mid + 1


