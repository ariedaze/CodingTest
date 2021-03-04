import sys
sys.stdin = open("input.txt","r")

N,M = map(int,input().split())
cnt = 0

# 핵심은 나이트가 오른쪽으로 밖에 가지 못한다.
# 두가지로 나눠서 처리, 4방식을 전부 채용해야하는 경우와 아닌경우로 나눠서 처리해야한다.
if N == 1 and M == 1:
    cnt = 1
elif N == 2: #N이 2이면 2번과 3번째 방법 밖에 쓸수 없다.
    cnt = (M+1)// 2

print(cnt)

