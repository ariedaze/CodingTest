def dfs(x, y):
    global count

    if x <= -1 or x >= N or y <= -1 or y >= N:
        return 0, count

    if arr[x][y] == 1:
        arr[x][y] = 0
        count += 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y -1 )
        return 1, count
    return 0, count

count = 0
result = 0
count_list = []
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        a, b = dfs(i, j)
        if a == 1:
            result += 1
            count_list.append(count)
            count = 0

print(result)
count_list.sort()

for cnt in count_list:
    print(cnt)


