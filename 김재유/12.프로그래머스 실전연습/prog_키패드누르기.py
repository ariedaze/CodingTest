key_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ["*", 0, "#"]]

def distance(num, target):
    x, y = now_location(num)
    target_x, target_y = now_location(target)
    return abs(x - target_x) + abs(y - target_y)

def now_location(num):
    for i in range(4):
        for j in range(3):
            if key_board[i][j] == num:
                return [i, j]

def solution(numbers, hand):
    result = ""
    left = "*"
    right = "#"
    for num in numbers:
        if num in [1, 4, 7]:
            result += "L"
            left = num
        elif num in [3, 6, 9]:
            result += "R"
            right = num
        else:
            left_distance = distance(left, num)
            right_distance = distance(right, num)
            if left_distance < right_distance:
                result += "L"
                left = num
            elif left_distance > right_distance:
                result += "R"
                right = num
            else:
                if hand == "right":
                    result += "R"
                    right = num
                else:
                    result += "L"
                    left = num
    return result