import sys
sys.stdin = open("input.txt","r")

pay = int(input())
ans = 0
rest = 1000 - pay

coins = [500, 100, 50, 10, 5, 1]

for coin in coins:
    if rest >= coin:
        ans += rest // coin
        rest %= coin

print(ans)
