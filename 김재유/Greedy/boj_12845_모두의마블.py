import sys; sys.stdin =open('input_data/12845.txt')

N = int(input())
cards = list(map(int, input().split()))
result = sum(cards) + max(cards) * (N-2)
print(result)

