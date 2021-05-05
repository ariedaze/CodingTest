import sys
sys.stdin = open('input/boj_5585_거스름돈.txt', 'r')

money_list = [500, 100, 50, 10 ,5, 1]

given = 1000 - int(input())
count = 0

for i in money_list:
    while given != 0 and given >= i:
        given -= i
        count += 1

print(count)
