import sys
sys.stdin = open("input.txt","r")

t = 0
while True:
    L, P, V = map(int, input().split())  # 연속하는 P일중 L일동안만 사용했다. 막 V일짜리 휴가를 시작했다.

    if (L == 0 and P == 0 and V == 0):
        break

    div = V // P

    rest = V - div * P

    ans = div * L + rest
    t += 1

    print("Case {}: {}".format(t, ans))

