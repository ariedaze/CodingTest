import sys
sys.stdin = open('input/boj_2231_분해합.txt', 'r')

N = int(input())
result = 0

for i in range(N, 0, -1):
    if i + sum(list(map(int, str(i)))) == N:
        result = i

print(result)

