import sys
sys.stdin = open('input/boj_2579_계단오르기.txt', 'r')

N = int(input())
score = [int(input()) for _ in range(N)]
score += [0, 0, 0]

result = [0]*(N+3)
result[0] = score[0]
result[1] = score[1]+score[0]
result[2] = max(score[0]+score[2], score[1]+score[2])

for stair in range(3, N):
    result[stair] = max(result[stair-2]+score[stair], result[stair-3]+score[stair]+score[stair-1])

print(result[N-1])
