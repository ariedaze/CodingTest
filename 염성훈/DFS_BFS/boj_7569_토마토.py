import sys
from collections import deque
sys.stdin = open("input.txt","r")

m,n,h = map(int,input().split())
arr = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

print(arr)