import sys
ln = sys.stdin.readline

N = int(ln())
lst = list(map(int, ln().split()))

flag = 0
cnt = 0
for i in range(N):
    if lst[i] == 0 and flag == 0:
        cnt += 1
        flag = 1
        continue
    if lst[i] == 1 and flag == 1:
        cnt += 1
        flag = 2
        continue
    if lst[i] == 2 and flag == 2:
        cnt += 1
        flag = 0
print(cnt)