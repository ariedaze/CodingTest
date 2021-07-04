def solution(arr):
    result = [0, 0]
    def quad(start_x, end_x, start_y, end_y):
        print(start_x, end_x, start_y, end_y)
        standard = arr[start_x][start_y]
        if end_x - start_x <= 1 or end_y - start_y <= 1:
            result[standard] += 1
            return
        for x in range(start_x, end_x):
            for y in range(start_y, end_y):
                if arr[x][y] != standard:
                    quad(start_x, (start_x + end_x)//2, start_y, (start_y + end_y)//2)
                    quad(start_x, (start_x + end_x)//2, (start_y + end_y)//2, end_y)
                    quad((start_x + end_x)//2, end_x, start_y, (start_y + end_y)//2)
                    quad((start_x + end_x)//2, end_x, (start_y + end_y)//2, end_y)
                    return
        result[standard] += 1

    quad(0, len(arr), 0, len(arr))

    return result
