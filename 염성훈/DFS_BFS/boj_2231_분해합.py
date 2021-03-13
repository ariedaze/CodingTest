import sys
sys.stdin = open("input.txt", "r")

N = int(input())

ans = 0

for i in range(1, N + 1):
    number_list = list(map(int,str(i))) #숫자를 하나씩 구분한다.
    total = i + sum(number_list)

    if total == N:
        ans = i
        break

print(ans)