import sys
sys.stdin = open('input/boj_12907_동물원.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))
total = [0] * 41
ex_total = 2

for a in arr:
    total[a] += 1

tmp = True
for cnt in total:
    if cnt > ex_total:
        tmp = False
        break
    ex_total = cnt

if tmp:
    print(2 ** (total.count(2) + (1 if 1 in total else 0)))
else:
    print(0)