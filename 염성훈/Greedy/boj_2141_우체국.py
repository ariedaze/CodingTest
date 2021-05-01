import sys
sys.stdin = open("input.txt","r")
# 사람수의 중간값을 찾으면 되는문제 였다. 처음에는 일일이 다 계산해줬음
# 중간 값의 의미 : 전체 사람수의 절반의 값인데 왜 이걸 활용해야하나?
# 중간값을 갖는 위치에 지으면 해당 인덱스에서 떨어진 거리의 가중치를 계산해 주지 않아도 됨
#1. 마을의 개수 : n
n=int(input())

#2. 마을의 위치, 인구 수 : info : [x,a]
info=[]
peoples=0 #전체 인구 수

for i in range(n):
    x=list(map(int,input().split()))
    info.append(x)
    peoples += x[1]

#3. 마을 위치 순으로 정렬
info.sort(key=lambda x:x[0])

mid = peoples//2

if (peoples%2) == 1:
    mid += 1

count = 0
for home, people in info:
   count += people

   if count >= mid:
       print(home)
       break


