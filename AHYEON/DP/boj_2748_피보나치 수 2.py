import sys
sys.stdin = open('input/boj_2748_피보나치 수 2.txt', 'r')

N = int(input())

result = [0]*(N+1)
result[1] = 1

for i in range(2, N+1):
    result[i] = result[i-1] + result[i-2]

print(result[N])