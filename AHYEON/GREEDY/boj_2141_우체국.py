N = int(input())


X = []
people = 0

for i in range(N):
    x = list(map(int, input().split()))
    X.append(x)
    people += x[1]

X.sort()
mid = people//2

if (people%2) == 1:
    mid += 1

cnt = 0
for x, p in X:
    cnt += p
    if cnt >= mid:
        print(x)
        break
