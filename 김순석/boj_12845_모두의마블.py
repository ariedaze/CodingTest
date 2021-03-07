import sys
In = sys.stdin.readline

N = int(In())
card = list(map(int, In().split()))

result = sum(card) + (max(card) * (N - 2))
print(result)