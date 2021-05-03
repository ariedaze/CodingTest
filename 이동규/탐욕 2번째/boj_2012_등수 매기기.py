import sys
sys.stdin = open('input/boj_2012_등수 매기기.txt', 'r')

N = int(input())
result = 0

L = [int(input()) for _ in range(N)]
L.sort()

for i, v in enumerate(L):
    result += abs(i+1 - v)

print(result)

