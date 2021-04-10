import sys
sys.stdin = open('input/boj_9095_123더하기.txt', 'r')

for _ in range(int(input())):
    n = int(input())
    result = [0]*(n+1)
    result[0] = 1

    for i in range(n+1):
        for step in range(1, 4):
            next = i + step
            if next > n: continue
            result[next] += result[i]

    print(result[n])