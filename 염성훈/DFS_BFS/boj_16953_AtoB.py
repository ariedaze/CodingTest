import sys
sys.stdin = open("input.txt","r")
from collections import deque

def bfs(x, cnt):
    Q = deque([x,cnt])

    while Q:
        source, number = Q.popleft()

        if source == B:
            return number + 1








A, B = map(int,input().split())

bfs(A, 0)