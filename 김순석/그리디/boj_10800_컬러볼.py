import sys
ln = sys.stdin.readline

N = int(ln())
arr = []
for i in range(N):
    C, S = map(int, ln().split())
    arr.append([i, C, S])

arr.sort(key=lambda x: x[2])
print(arr)

sum_val = 0
temp = 0
lst = []
for i in range(N):
    if i == N - 1:
        lst.append([arr[i][0], sum_val])
        continue

    if arr[i][2] < arr[i + 1][2] and arr[i][1] != arr[i+1][1]:
        sum_val += temp
        temp = arr[i][2]
        lst.append([arr[i][0], sum_val])

print(lst)

