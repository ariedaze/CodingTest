
def find_way(position, result, go_list):
    global move_min
    if result > move_min:
        return
    if go_list:
        go_right = list(go_list)
        go_left = list(go_list)
        right = go_right.pop(0)
        left = go_left.pop()
        #정방향
        find_way(right, result+abs(right-position), go_right)
        find_way(right, result+(len(name) - abs(right-position)), go_right)
        #역방향
        find_way(left, result+abs(left-position), go_left)
        find_way(left, result+(len(name) - abs(left-position)), go_left)
    else:
        if move_min > result:
            move_min = result


name = "JAN"
result = 0
name_length = len(name)
go_list = []
move_min = 0xffffff
now = 0
depth = 1



for idx, char in enumerate(name):
    count = ord(char) - ord('A')
    if count > 13:
        result += 26 - count
    else:
        result += count
    if count and idx:
        go_list.append(idx)

find_way(0, result, go_list)

print(move_min)
