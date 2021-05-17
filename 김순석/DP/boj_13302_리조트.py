# 64, 3044, 72, 2980,
import sys
ln = sys.stdin.readline

# 3일 2.5, 쿠폰 1장
# 5일 3.7, 쿠폰 2장
# 5

N, M = map(int, ln().split())

min_val = 0xfffffff
c = (N // 5) * 2 + 2

dp = [[min_val] * (N + 1) for _ in range(N + 1)]
if M != 0:
    lst = list(map(int, ln().split()))
    check = [0] * (N + 1)
    for i in lst:
        check[i] = 1
else:
    check = [0] * (N + 1)

def calc(day, coupon, price):
    if N < day:
        return price
    if dp[day][coupon] != min_val:
        return dp[day][coupon] + price
    if check[day]:
        return calc(day + 1, coupon, price)

    ans = min(min_val, calc(day + 1, coupon, price + 10000))
    ans = min(ans, calc(day + 3, coupon + 1, price + 25000))
    ans = min(ans, calc(day + 5, coupon + 2, price + 37000))

    if coupon >= 3:
        ans = min(ans, calc(day + 1, coupon - 3, price))

    dp[day][coupon] = ans - price
    return ans


print(calc(1, 0, 0))

