import sys
sys.stdin = open("input.txt","r")
from collections import deque

def bfs(A, cnt):
    Q = deque([(A,cnt)])

    while Q:
        source, number = Q.popleft()
        if source == B:
            return number + 1
        if source*2 <= B:
            Q.append((source*2, number + 1))
        if int(str(source)+'1') <= B:
            Q.append((int(str(source)+'1'), number + 1))


A, B = map(int,input().split())

ans = bfs(A, 0)

if ans:
    print(ans)
else:
    print(-1)