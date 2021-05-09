import sys
sys.stdin = open("input.txt","r")
from collections import deque

def bfs(a):
    q = deque()
    q.append(a)
    count = [-1] * 10000
    count[a] = ""

    while q:
        x = q.popleft()

        if x == B:
            return count[B]
        #D
        no,nx = divmod(2*x, 10000)
        if count[nx] == -1:
            count[nx] = count[x] + 'D'
            q.append(nx)

        #S
        if x == 0:
            nx = 9999
        else:
            nx = x - 1

        if count[nx] == -1:


T = int(input())

for _ in range(T):
    A, B = map(str,input().split()) #A: 시작값 B: 최종값
    bfs(A)

