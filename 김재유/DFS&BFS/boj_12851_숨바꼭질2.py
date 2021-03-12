import sys; sys.stdin = open('input_data/12851.txt')
sys.setrecursionlimit(100000)

def DFS(number, depth):
    global fast
    global result
    if depth > fast: return
    if target == number:
        if fast > depth:
            fast = depth
            result = 1
        elif fast == depth:
            result += 1
    else:
        DFS(number*2, depth+1)
        DFS(number+1, depth+1)
        DFS(number-1, depth+1)

now, target = map(int, input().split())
fast = target-now
result = 0
DFS(now, 0)
print(fast)
print(result)
