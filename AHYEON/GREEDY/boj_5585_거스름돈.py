M = int(input())
money = 1000 - M

cnt = 0

for coin in [500, 100, 50, 10, 5, 1]:
    cnt += money // coin
    money %= coin


print(cnt)
