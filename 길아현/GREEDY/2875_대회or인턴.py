N, M, K = map(int, input().split())
people_num = N + M - K
result = 0
while True:
    people_num -= 3
    if people_num >= 0 and N-2 >= 0 and M-1 >= 0:
        result += 1
        N -= 2
        M -= 1
    else:
        break

print(result)
