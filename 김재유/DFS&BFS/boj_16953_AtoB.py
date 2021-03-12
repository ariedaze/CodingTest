import sys; sys.stdin = open('input_data/16953.txt')

def DFS(number, depth):
    global depth_list
    if number > end: return
    if number == end:
        depth_list.append(depth)
    DFS(number*2, depth + 1)
    DFS(number*10 + 1, depth + 1)


start, end = map(int, input().split())
depth_list =[]
DFS(start, 1)
if depth_list:
    print(min(depth_list))
else:
    print(-1)
