import sys
ln = sys.stdin.readline

N = int(ln())
sum_val = 0
arr = []
for _ in range(N):
    X, A = map(int, ln().split())
    arr.append([X, A])
    sum_val += A
arr.sort()
mid = sum_val / 2

cnt = 0
for i in range(N):
    cnt += arr[i][1]
    if cnt >= mid:
        print(arr[i][0])
        break