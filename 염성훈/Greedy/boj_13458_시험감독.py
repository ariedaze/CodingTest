import sys
sys.stdin = open("input.txt", "r")

N = int(input()) #시험장의 수
persons = list(map(int,input().split()))
first, sub = map(int,input().split())
ans = 0

for i in range(N):
    if persons[i] - first > 0:
        ans += 1
        temp = persons[i] - first
        if temp % sub:
            ans += (temp // sub) + 1
        else:
            ans += (temp // sub)

    else :
        ans += 1

print(ans)

