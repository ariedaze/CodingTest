import sys
sys.stdin = open("input.txt","r")

ex, ey, s, w = map(int,input().split()) # S : 가로, 세로 이동 W: 대각선 이동시간
# 첫 풀이 이렇게 하면 대각선 이동이 가로 세로 이동보다 2배 아래일때 경우의 수를
# 놓치게 된다.
# if s <= w*2:
#     ans += min(ex,ey) * w
#     ans += abs(ex-ey) * s
# else:
#     ans += (ex + ey) * s
# 2가지 경우로 나눠야한다. 평행이동과 대각선 + 평행이동
move1 = (ex + ey) * s

if (ex +ey) % 2:
    move2 = (max(ex,ey) -1)*w +s
else:
    move2 = max(ex,ey) * w

move3 = (min(ex,ey) * w) + ((max(ex,ey) - min(ex,ey)) * s)

ans = min(min(move1,move2), move3)

print(ans)