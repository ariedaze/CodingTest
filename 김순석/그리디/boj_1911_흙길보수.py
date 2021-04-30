# 시간초과나서 pypy로 제출함
import sys

ln = sys.stdin.readline

N, L = map(int, input().split())
arr = []
for _ in range(N):
    s, e = map(int, input().split())
    arr.append([s, e])

arr.sort(key=lambda x: x[0])

cnt = 0
pivot = 0

for i in range(N):
    s, e = arr[i][0], arr[i][1]

    if s > pivot:
        pivot = s

    while e > pivot:
        pivot += L
        cnt += 1

print(cnt)