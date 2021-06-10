keyPad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]


def now_location(num):
    for x in range(4):
        for y in range(3):
            if keyPad[x][y] == num:
                return [x, y]

def solution(numbers, hand):
    answer = []
    now_L = [3, 0]
    now_R = [3, 2]

    for num in numbers:
        if num == 1 or num == 4 or num == 7:
            answer.append('L')
            now_L = now_location(num)
        elif num == 3 or num == 6 or num == 9:
            answer.append('R')
            now_R = now_location(num)
        else:
            for x in range(4):
                for y in range(3):
                    if keyPad[x][y] == num:
                        if abs(now_L[0] - x) + abs(now_L[1] - y) > abs(now_R[0] - x) + abs(now_R[1] - y):
                            answer.append('R')
                            now_R = now_location(num)
                        elif abs(now_L[0] - x) + abs(now_L[1] - y) < abs(now_R[0] - x) + abs(now_R[1] - y):
                            answer.append('L')
                            now_L = now_location(num)
                        else:
                            if hand == "right":
                                answer.append('R')
                                now_R = now_location(num)
                            else:
                                answer.append('L')
                                now_L = now_location(num)

    return "".join(answer)

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
solution(numbers, hand)