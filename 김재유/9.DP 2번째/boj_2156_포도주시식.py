import sys; sys.stdin = open('input_data/2156.txt')
from pprint import pp

N = int(input())
wines = [0] +[int(input()) for _ in range(N)]
# 3개로 나눠서 선택X, 전선택 X 이번선택 O, 전, 이번 둘다 선택 구분
check = [[0]*(N+1) for _ in range(3)]

check[1][1] = wines[1]
for i in range(2, N+1):
    # 연속으로 먹는 건, 전 잔 먹고 + 이번 거
    check[2][i] = check[1][i-1] + wines[i]
    # 안먹는 건 , 연속 2잔과 전 것만 먹은거 중에 큰값
    check[0][i] = max(check[1][i-1], check[2][i-1], check[1][i-2], check[2][i-2])
    # 이번에만 먹는 건, 전에 안먹고 + 이번 거
    check[1][i] = max(check[0][i-1], check[0][i-2]) + wines[i]

pp(check)

print(max(check[2][N], check[1][N], check[0][N]))