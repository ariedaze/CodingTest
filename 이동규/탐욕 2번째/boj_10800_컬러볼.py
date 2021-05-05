import sys

sys.stdin = open('input/boj_10800_컬러볼.txt', 'r')

n = int(input())
ball = []
answer = dict()
ball_size_sum = dict()
for i in range(n):
    answer[i] = 0
    ball_size_sum[i] = 0
    c, s = map(int, input().split())
    ball.append([c, s, i])

# 공의 크기 순으로 정렬
ball.sort(key=lambda x: x[1])

answer = dict()
ball_size_sum = dict()  # 색깔 별 공의 크기 누적합

total = 0  # 총합
i, j = 0, 0
for i in range(n):
    while ball[j][1] < ball[i][1]:  # 크기가 작을 때까지 수행
        total += ball[j][1]
        ball_size_sum[ball[j][0]] += ball[j][1]
        j += 1
    answer[ball[i][2]] = total - ball_size_sum[ball[i][0]]  # 총합 - 현재 색깔 공 누적합

for i in range(n):
    print(answer[i])