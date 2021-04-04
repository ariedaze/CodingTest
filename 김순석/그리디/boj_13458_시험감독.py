import math

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
C_cnt = 0
for a in A:
    if a > B:
        C_cnt += math.ceil((a - B) / C)

print(N + C_cnt)