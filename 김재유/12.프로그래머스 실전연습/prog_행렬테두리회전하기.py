rows = 100
columns = 97
queries = [[1,1,100,97]]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

Ground = [[0]*columns for _ in range(rows)]
num = 1
for i in range(rows):
    for j in range(columns):
        Ground[i][j] = num
        num += 1
result = []
def circle(query):
    query = list(map(lambda x: x-1, query))
    start_x, start_y, end_x, end_y = query
    keep = Ground[start_x][start_y]
    min_check = []
    change_list = []
    for i in range(start_y, end_y):
        change_list.append([start_x, i])
        min_check.append(Ground[start_x][i])
    for i in range(start_x, end_x):
        change_list.append([i, end_y])
        min_check.append(Ground[i][end_y])
    for i in range(end_y, start_y, -1):
        change_list.append([end_x, i])
        min_check.append(Ground[end_x][i])
    for i in range(end_x, start_x, -1):
        change_list.append([i, start_y])
        min_check.append(Ground[i][start_y])
    change_list.append(change_list.pop(0))

    for change in change_list:
        x, y = change
        Ground[x][y], keep = keep, Ground[x][y]
    return min(min_check)
for query in queries:
    result.append(circle(query))
print(result)
