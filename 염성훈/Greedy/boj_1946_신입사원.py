import sys

T = int(input())
for t in range(1,T+1):
    N = int(input())
    peoples = [tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]

    peoples.sort(key=lambda x: x[0]) #첫번째 순위별로 정렬

    cnt = 1

    min_value = peoples[0][1]
    for i in range(1,N):
        if peoples[i][1] < min_value:
            min_value = peoples[i][1]
            cnt += 1

    print(cnt)




