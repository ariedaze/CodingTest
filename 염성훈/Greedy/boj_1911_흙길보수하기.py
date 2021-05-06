import sys
import math
sys.stdin = open("input.txt", "r")

N, L = map(int,input().split()) #N: 웅덩이의 갯수 L: 널판지의 길이

arr = [tuple(map(int,input().split())) for _ in range(N)]

arr.sort()
temp, s = 0,0

for i in range(N):
    ## 시작지점 정하고
    s = max(arr[i][0],s)
    #시작지점에서 물웅덩이를 매우기 위한 길이를 구한다.
    diff = arr[i][1] - s
    # 웅덩이를 매우기 이한 널판지의 갯수를 구한다. 올림 처리를 위해 ceil 사용
    count = math.ceil(diff/L)
    temp += count
    s += count * L

print(temp)






