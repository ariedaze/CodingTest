def dfs(depth, begin, partsum):
    global result
    if depth == N:
        if ans.get(partsum):
            return
        else:
            ans[partsum] = 1
            result += 1
            return

    for i in range(begin, 4):
        dfs(depth+1, i, partsum + num_list[i])


N = int(input())
num_list = [1, 5, 10, 50]
ans = {}
result = 0
dfs(0, 0, 0)
print(result)
