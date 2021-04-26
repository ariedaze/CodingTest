import sys


input = sys.stdin.readline

N = int(input())
score = [int(input()) for _ in range(N)]


score.sort()

angry = 0
for i in range(1, N+1):
    angry += abs(score[i-1] - i)

print(angry)