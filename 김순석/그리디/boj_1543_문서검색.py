import sys
ln = sys.stdin.readline

S = input()
W = input()

s, w = len(S), len(W)
ans = 0
pivot = 0
for i in range(s):
    if W == S[i+pivot:i+w+pivot]:
        ans += 1
        pivot += w - 1

print(ans)