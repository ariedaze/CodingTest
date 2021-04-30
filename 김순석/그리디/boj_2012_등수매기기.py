import sys
ln = sys.stdin.readline

N = int(ln())
rank = [0] + [int(ln()) for _ in range(N)]
rank.sort()

ans = 0
for i in range(N+1):
    ans += abs(i-rank[i])

print(ans)