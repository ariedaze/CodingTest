import sys
sys.stdin = open("input.txt","r")

N = int(input())

max_weight = 0

ropes = [int(input()) for _ in range(N)]

ropes.sort(reverse=False)

for i in range(len(ropes)):
    temp = ropes[i] * N
    if max_weight < temp:
        max_weight = temp
    N -= 1

print(max_weight)
