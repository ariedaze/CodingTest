import sys
sys.stdin = open("input.txt","r")

from itertools import permutations

n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

num = list(permutations(n,3))

length = len(num)
print(length)


N = int(input())

for _ in range(N):
    numbers, strike, ball = map(int,input().split())


