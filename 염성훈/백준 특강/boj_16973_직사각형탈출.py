import sys
sys.stdin = open("input.txt","r")

N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

H, W, Sr, Sc, Fr, Fc = map(int,input().split())
Sr += -1
Sc += -1
Fr += -1
Fc += -1 

