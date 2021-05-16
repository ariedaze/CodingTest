import sys; sys.stdin = open('input_data/14722.txt')

size = int(input())
Ground = [list(map(int, input().split())) for _ in range(size)]
check = [[0]*size for _ in range(size)]
now = 0
for i in range(size):
    for j in range(size):
        if i == 0 and j == 0:
            if Ground[i][j] == now:
                check[i][j] = now+1
        elif i == 0:
            stack = check[i][j-1]
            now = stack%3
            if Ground[i][j] == now:
                check[i][j] = stack+1
            else:
                check[i][j] = stack
        elif j == 0 :
            stack = check[i-1][j]
            now = stack%3
            if Ground[i][j] == now:
                check[i][j] = stack+1
            else:
                check[i][j] = stack
        else:
            stack = max(check[i-1][j], check[i][j-1])
            now = stack % 3
            if Ground[i][j] == now:
                check[i][j] = stack+1
            else:
                check[i][j] = stack
print(check[size-1][size-1])


