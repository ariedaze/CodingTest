N = int(input())
left = 1
right = N
mid = (left+right) // 2

while left <= right:
    midsquared = mid ** 2
    if midsquared == N:
        break
    elif midsquared < N:
        left = mid
        mid = (left + right) // 2
    elif midsquared > N:
        right = mid
        mid = (left + right) // 2

print(mid)