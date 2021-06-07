import sys
sys.stdin = open('input/boj_1459_걷기.txt', 'r')

X, Y, W, S = list(map(int, input().split()))

if (2*W) >= S:
    result = min(X,Y)*S
    if S < W:
        result += ((abs(X-Y) // 2) * 2 * S) + ((abs(X-Y) % 2) * W)
    else:
        result += (abs(X-Y)*W)
    print(result)
else:
    print((X+Y)*W)
