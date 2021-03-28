import sys
sys.stdin = open("input.txt","r")
N = int(input())

stair = []

for i in range(N):
    stair.append(int(input().strip()))

d = []
d.append(stair[0])

if N == 1:
    print(d[0])
elif N == 2:
    d.append(max(stair[0] + stair[1], stair[1]))
    print(d[-1])
else :
    for i in range(1,3):
        if i == 1:
            d.append(max(d[i - 1] + stair[i], stair[i]))
            continue
        d.append(max(stair[i] + stair[i - 1], stair[i] + d[i - 2]))


    for i in range(3, N):
        d.append(max(stair[i] + d[i - 2], stair[i] + stair[i - 1] + d[i - 3]))

    print(d[-1])



