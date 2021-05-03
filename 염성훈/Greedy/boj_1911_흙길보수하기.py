import sys
sys.stdin = open("input.txt", "r")

N, L = map(int,input().split()) #N: 웅덩이의 갯수 L: 널판지의 길이

arr = [tuple(map(int,input().split())) for _ in range(N)]

arr.sort()
temp, s = 0,0

for i in range(N):
    s = max(arr[i][0],s)
    print(s)







