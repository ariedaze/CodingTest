import sys; sys.stdin = open('input_data/11047.txt')

N, total = map(int, input().split())
coin_list = [int(input()) for _ in range(N)][::-1]
result = 0
for coin in coin_list:
    result += total//coin
    total -= total//coin * coin
print(result)