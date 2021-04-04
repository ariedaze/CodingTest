import sys
In = sys.stdin.readline

N, K = map(int, In().split())

lst = [int(In()) for i in range(N)]
idx = 0
cnt = 0
while K != 0:
    if lst[-1] > K:
        for i in range(N):
            if lst[i] == K:
                cnt += 1
                K = 0
                break

            elif lst[i] > K:
                idx = i - 1
                Q = K // lst[idx]
                R = K % lst[idx]

                cnt += Q
                K = R
                break

    elif lst[-1] < K:
        Q = K // lst[-1]
        R = K % lst[-1]

        cnt += Q
        K = R

    else:
        cnt += 1
        break

print(cnt)
