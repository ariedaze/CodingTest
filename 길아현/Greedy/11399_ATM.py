N = int(input())
P = list(map(int, input().split()))

P.sort()
result = 0
for n in range(N, 0, -1):
    result += n*P[N-n]

print(result)