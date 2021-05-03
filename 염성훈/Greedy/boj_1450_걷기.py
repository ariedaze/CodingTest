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
# 해당 점에 갈 수 있는 전체 방법을 계산하고 그중에서의 최소값을 뽑는 식으로한다.
# 평행이동하는 경우
move1 = (ex + ey) * s

# 대각선 + 평행이동의 경우
if (ex + ey) % 2:
    move2 = (max(ex,ey) -1)*w +s
# 짝수일때 대각선으로만으로 움직일 수 있음.
else:
    move2 = max(ex,ey) * w

move3 = (min(ex,ey) * w) + ((max(ex,ey) - min(ex,ey)) * s)

ans = min(min(move1,move2), move3)

print(ans)