import sys
sys.stdin = open('input/boj_2503_숫자야구.txt', 'r')

def dfs():
    pass

N = int(input())
ball_count = []
strike = []
ball = []

first_visit = [True for _ in range(9)]
second_visit = [True for _ in range(9)]
third_visit = [True for _ in range(9)]


for _ in range(N):
    a, b, c = list(map(int, input().split()))
    ball_count.append(list(map(int, str(a))))
    strike.append(b)
    ball.append(c)

if 3 in strike:
    print(1)

