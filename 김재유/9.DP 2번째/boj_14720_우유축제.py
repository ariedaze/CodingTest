import sys; sys.stdin = open('input_data/14720.txt')

N = int(input())
result = 0
stores = list(map(int, input().split()))
for i in range(N):
    if result%3 == stores[i]:
        result += 1
print(result)