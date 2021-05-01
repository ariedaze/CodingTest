import sys
sys.stdin = open("input.txt","r")
# 1. 양수와 음수로 두가지 리스트로 나누고 두개를 높은순으로 정렬시킴
# 2. 정렬시킨 값에서 두개씩 뺴서 최종값에 다가 더해주고 만약 한개가 남았다면 그냥 하나를 뺴서 더해준다.
n = int(input())
minus_list = []
plus_list = []
ans = 0

# 플러스, 마이너스로 나누고
for _ in range(n):
    k = int(input())
    if k > 0:
        plus_list.append(k)
    else:
        minus_list.append(k)
#정렬
minus_list.sort()
plus_list.sort(reverse=True)


# 이렇게 하면 복잡쓰
# if m % 2:
#     ans += minus_list[-1]
#     for i in range(0, m - 1, 2):
#         ans += minus_list[i] * minus_list[i+1]
# else:
#     for i in range(0, m, 2):
#         ans += minus_list[i] * minus_list[i + 1]
#
# if p % 2:
#     ans += plus_list[-1]
#     for i in range(0, p - 1, 2):
#         ans += plus_list[i] * plus_list[i + 1]
# else:
#     if plus_list:
#         if plus_list[-1] == 1:
#             ans += plus_list[-1] + plus_list[-2]
#             for i in range(0, p - 2, 2):
#                 ans += plus_list[i] * plus_list[i + 1]
#         else:
#             for i in range(0, p, 2):
#                 ans += plus_list[i] * plus_list[i + 1]

# pop 사용
while minus_list:
    first = minus_list.pop(0)
    if minus_list:
        second = minus_list.pop(0)
        ans += first * second
    else:
        ans += first

while plus_list:
    first = plus_list.pop(0)
    if plus_list:
        second = plus_list.pop(0)
        #양수에서는 마지막 값이 1일때 곱하는 것보다 두 수를 더해주는 것이 더 값이 큼
        if second == 1:
            ans += first + second
        else :
            ans += first * second
    else:
        ans += first

print(ans)

