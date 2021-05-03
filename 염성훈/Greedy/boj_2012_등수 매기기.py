import sys
sys.stdin = open("input.txt","r")

#python3으로 하니까 시간초과나오는데 pypy3로 하니까 됨. 왠지는 몰겠음.
N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()

ans = 0
for i in range(1, N + 1):
    ans += abs(i - arr[i - 1])

print(ans)