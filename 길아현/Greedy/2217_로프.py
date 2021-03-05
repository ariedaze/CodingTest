N = int(input())

weights = [int(input()) for _ in range(N)]
weights.sort()
answer = 0
for i in range(N):
    answer = max(answer, weights[i]*(N-i))
print(answer)
