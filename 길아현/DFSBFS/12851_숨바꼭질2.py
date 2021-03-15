from collections import deque

N, K = map(int, input().split())  # N: 수빈, K: 동생


ways = [0]*100001; ways[N] = 1
times = [100000000]*100001; times[N] = 0

if N >= K:
    print(N-K); print(1)
else:
    Q = deque([N])
    while Q:
        here = Q.popleft()
        next_move = [here+1, here-1, here*2]
        for next in next_move:
            if 0 <= next <= 100000 and times[next] >= times[here]+1:
                Q.append(next)
                ways[next] += 1
                times[next] = times[here]+1
    print(times[K])
    print(ways[K])

