import sys
from pprint import pprint
sys.stdin = open('input_data/2606.txt')

# DSF 함수만들기
def DSF(x):
    visit[x] = 1  # 방문한곳 1로 바꾸기
    for i in range(1, dot+1): # [1,i] 로 연결된 선 찾아보기
        if ground[x][i] and not visit[i]:  #연결되어있고, 방문하지 않았으면
            DSF(i)                          # 가자!

# data input
dot = int(input())
line = int(input())
line_data = [list(map(int,input().split())) for _ in range(line)]

# 연결선 지도와
ground = [[0] * (dot+1) for _ in range(dot+1)]
for data in line_data:
    ground[data[0]][data[1]] = 1
    ground[data[1]][data[0]] = 1
# 방문일지 작성하기
visit = [0]* (dot+1)

#함수 돌리기
DSF(1)

print(visit.count(1)-1)


