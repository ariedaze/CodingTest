N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

lst = sorted(lst, key=lambda x: (x[1], x[0]))

cnt = 0
time = 0

for i in lst:
    if time <= i[0]:
        cnt += 1
        time = i[1]

print(cnt)
