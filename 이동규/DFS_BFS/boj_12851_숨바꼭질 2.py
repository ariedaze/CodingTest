import sys
sys.stdin = open('input/boj_12851_숨바꼭질 2.txt', 'r')

def dfs(num, count):
    global MIN, duplicat_num

    if num > B * 2:
        return
    if num == B and count < MIN:
        MIN = count
        duplicat_num = 1
    if num == B and count == MIN:
        duplicat_num += 1


    if 0 <= num*2 < 100001 and visit[num*2] > count:
        visit[num*2] = count
        dfs(num*2, count+1)

    if 0 <= num + 1 < 100001 and visit[num + 1] > count:
        visit[num + 1] = count
        dfs(num + 1, count + 1)

    if 0 <= num - 1 < 100001 and visit[num - 1] > count:
        visit[num - 1] = count
        dfs(num - 1, count + 1)

A, B = list(map(int, input().split()))
MIN = 99999
visit = [99999 for _ in range(100001)]
visit[A] = 0
duplicat_num = 1

dfs(A, 0)

if MIN == 99999:
    print(-1)
else:
    print(MIN)
    print(duplicat_num)