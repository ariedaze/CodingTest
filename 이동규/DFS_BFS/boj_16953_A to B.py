import sys
sys.stdin = open('input/boj_16953_A to B.txt', 'r')

def dfs(num, count):
    global MIN

    if num > B:
        return
    if num == B and count < MIN:
        MIN = count

    dfs(num*2, count+1)

    dfs(int(str(num)+'1'), count+1)

A, B = list(map(int, input().split()))
MIN = 99999

dfs(A, 1)

if MIN == 99999:
    print(-1)
else:
    print(MIN)
