import sys
sys.stdin = open("input.txt","r")
N = list(input())
N.sort(reverse=True)
max_value = 0


for i in N:
    max_value += int(i)

# 30의 배수는 각자리 숫자의 합이 3의 배수이거나 1의 자리 숫자가 0이어야한다.
if max_value % 3 != 0 or "0" not in N:
    print(-1)
else:
    print("".join(N))
