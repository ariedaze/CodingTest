N = int(input())
street = input()
dp = [987654321] * N

dp[0] = 0

for i in range(1, N):
    here = street[i]
    prev = ''
    if here == 'B':
        prev = 'J'
    elif here == 'O':
        prev = 'B'
    elif here == 'J':
        prev = 'O'

    for j in range(i):
        if street[j] == prev:
            dp[i] = min(dp[i], dp[j] + (i-j)**2)


if dp[N-1] == 987654321:
    print(-1)
else:
    print(dp[N-1])