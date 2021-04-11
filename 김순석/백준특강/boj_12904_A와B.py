import sys
ln = sys.stdin.readline

S = ln().strip()
T = ln().strip()

s = len(S)
ans = 0
while s <= len(T):
    if T[-1] == 'A':
        T = T[:-1]
    elif T[-1] == 'B':
        T = T[:-1]
        T = T[::-1]
    if T == S:
        ans = 1
print(ans)