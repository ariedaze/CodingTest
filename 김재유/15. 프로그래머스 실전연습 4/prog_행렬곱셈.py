arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4], [2, 4], [3, 1]]
size = len(arr2)
height = len(arr1)
width = len(arr2[0])
result = [[0]*width for _ in range(height)]
for i in range(height):
    for j in range(width):
        num = 0
        for k in range(size):
            num += arr1[i][k] * arr2[k][j]
        result[i][j] = num
print(result)