## 이게 당최 뭔소린지 이해가 되질 않아
## 쭈냄 코드 참고


import sys; sys.stdin = open('input_data/13302.txt')

def DFS(day, coupon) :
    if day > days:
        return 0
    if check[day][coupon] == 0xffffff:
        if off_day[day]:
            check[day][coupon] = DFS(day+1, coupon)
        else:
            price = [DFS(day+1, coupon) + 10000, DFS(day+3, coupon+1) + 25000, DFS(day+5, coupon+2) + 37000]
            if coupon > 2:
                price.append(DFS(day+1, coupon-3))
            check[day][coupon] = min(price)

    return check[day][coupon]

days, off_num = map(int, input().split())
if off_num:
    off = list(map(int, input().split()))
    off_day = [0]*(days+1)
    for i in off:
        off_day[i] = 1
check = [[0xffffff] * (days+1) for _ in range(days+1)]
print(DFS(1, 0))








