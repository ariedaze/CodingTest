import sys; sys.stdin = open('input_data/11399.txt')

ATM = int(input())
times = list(map(int, input().split()))
times.sort(reverse=True)
result = 0
for idx, time in enumerate(times):
    result += time*(idx+1)
print(result)