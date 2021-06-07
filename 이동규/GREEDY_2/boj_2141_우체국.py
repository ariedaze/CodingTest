import sys
sys.stdin = open('input/boj_2141_우체국.txt', 'r')

# N = int(input())
# li = [[0,0]]
#
# min_idx = 0
# min_val = 999999999
#
# for i in range(N):
#     temp = list(map(int, input().split()))
#     li.append([temp[0], li[-1][1] + temp[1]])
# li.append(li[-1])
#
# for i in range(1, N+1):
#     temp = abs(li[i - 1][1] - (li[-1][1] - li[i][1]))
#     if temp < min_val:
#         min_val = temp
#         min_idx = li[i][0]
#
# print(min_idx)

n=int(input())

info=[]
people=0 #전체 인구 수

for i in range(n):
    x=list(map(int,input().split()))
    info.append(x)
    people+=x[1]

#3. 마을 위치 순으로 정렬
info=sorted(info)

#4. 인구의 절반 구하기
mid= (people//2) + 1 if (people%2)==1 else people//2

#5. 인구의 절반이 속한 마을에 우체국 설치
count=0
for l,p in info:
    count+=p

    if count>=mid:
        print(l)
        break

