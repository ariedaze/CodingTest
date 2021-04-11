import sys
sys.stdin = open("input.txt","r")

N = int(input())
arr = list(map(int, input().split()))
# 전체 몇명의 고양이가 대답했는지 파악한다.
total = [0] * 41
# 토끼와 고양이 둘밖에 없으므로 cnt가 2를 넘어가서는 안된다.
ex_total = 2

for a in arr:
    total[a] += 1

tmp = True
for cnt in total: #조건탐색
    if cnt > ex_total:
        tmp = False
        break
    ex_total = cnt

# 스트레이트로 올라가는 것은 2번 새줘야한다.
if tmp:
    print(2 ** (total.count(2) + (1 if 1 in total else 0)))
    print(total)
else:
    print(0)
