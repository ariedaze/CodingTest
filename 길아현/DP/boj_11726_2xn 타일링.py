import sys
sys.stdin = open('input/boj_11726_2xn 타일링.txt', 'r')

N = int(input())

result = [0]*(N+1)
result[1] = 1
result[2] = 2

for i in range(3, N+1):
    result[i] = (result[i-1]+result[i-2])

print(result[N] % 10007)