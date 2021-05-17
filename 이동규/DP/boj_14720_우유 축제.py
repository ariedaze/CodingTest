import sys
sys.stdin = open('input/boj_14720_우유 축제.txt', 'r')

N = int(input())
MILK_STORE = list(map(int, input().split()))

target = 0
result = 0
for i in MILK_STORE:
    if i == target:
        result += 1
        target = (target + 1) % 3

print(result)