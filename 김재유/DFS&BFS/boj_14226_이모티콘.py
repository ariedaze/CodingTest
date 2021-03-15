import sys; sys.stdin = open('input_data/14226.txt')
from collections import deque

N = int(input())
result = N
Q = deque()
Q.append([1, 0, 0])
visit = [0]*1000
while Q:
    n, depth, clipboard = Q.popleft()
    if depth >= result: continue
    if n == N:
        result = depth
        continue
    Q.append([n, depth+1, n])
    Q.append([n+clipboard, depth+1, clipboard])
    if n-1>0:
        Q.append([n-1, depth+1, clipboard])
print(result)


