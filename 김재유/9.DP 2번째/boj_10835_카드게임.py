import sys; sys.stdin = open('input_data/10835.txt')
from pprint import pprint


N = int(input())
check = [[0] * (N+1) for _ in range(N+1)]

left_list = list(map(int, input().split()))
right_list = list(map(int, input().split()))

if max(left_list) > max(right_list):
    print(sum(right_list))
    exit()

for left in range(N-1, -1, -1):
    for right in range(N-1, -1, -1):
        if left_list[left] > right_list[right]:
            check[left][right] = max(check[left][right+1] + right_list[right], check[left+1][right+1], check[left+1][right])
        else:
            check[left][right] = max(check[left+1][right+1], check[left+1][right])
print(check[0][0])






