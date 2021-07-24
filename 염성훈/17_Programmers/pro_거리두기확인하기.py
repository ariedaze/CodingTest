# def makearr(place):
#     arr = []
#     for line in place:
#         temp = []
#         for people in line:
#             temp.append(people)
#         arr.append(temp)
#     return arr

def check(x,y,arr):

    dir = [(1,0),(0,1),(-1,0),(0,-1)]
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if arr[nx][ny] == 'P':
            return False

    dir = [(-1,-1),(-1,1),(1,-1),(1,1)]
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if arr[nx][ny] == 'P' and (arr[x][ny] != 'X' or arr[nx][y] != 'X'):
            return False

    dir = [(2,0), (0,2), (-2,0), (0,-2)]
    for dx, dy in dir:
        nx, ny = x + dx, y + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if arr[nx][ny] == 'P' and arr[x + dx//2][y + dy//2] != 'X':
            return False

    return True

n = 5
def solution(places):
    answer = []
    for place in places:
        flag = False
        for r,c in [(i, j) for i in range(5) for j in range(5)]:
            if place[r][c] == 'P':
                result = check(r, c , place)

                if not result:
                    answer.append(0)
                    flag = True
                    break
        if not flag:
            answer.append(1)

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)