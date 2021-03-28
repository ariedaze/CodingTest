# import sys
# sys.stdin = open('input/boj_15486_퇴사2.txt', 'r')

N = int(input())
T = []
P = []
result = [0]*(N+1)

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

M = 0
for i in range(N):
    M = max(M, result[i])
    if i+T[i] > N: continue
    result[i+T[i]] = max(M+P[i], result[i+T[i]])
print(max(result))
