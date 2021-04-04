N = int(input())
time = list(map(int, input().split()))

time.sort(reverse=True)
ans = 0
for i in range(N):
    ans += time[i] * (i + 1)
print(ans)

