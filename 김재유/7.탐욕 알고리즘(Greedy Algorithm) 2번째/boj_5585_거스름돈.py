#TODO 파트 7

import sys; sys.stdin = open('input_data/5585.txt')

money = 1000 - int(input())

money_kind = [500, 100, 50, 10, 5, 1]

result = 0
for i in range(6):
    money_num = money//money_kind[i]
    money -= (money//money_kind[i] * money_kind[i])
    result += money_num
    if not money:
        break
print(result)