import sys
sys.stdin = open('input/boj_11722_가장 감소 수열.txt', 'r')

N = int(input())
A = list(map(int, input().split()))
memo = [1] * N

for i in range(N-1, -1, -1):
    temp_max = 0
    for j in range(i+1, N):
        if A[i] > A[j] and temp_max < memo[j]: # 뒤에서 부터 비교해서 현재 값이 더 크면
            temp_max = memo[j]
    memo[i] += temp_max

print(max(memo))
