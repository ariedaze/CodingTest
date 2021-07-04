n = 5
check = [0]*(n+1)
for i in range(1, n+1):
    if i < 3:
        check[i] = 1
    else:
        check[i] = check[i - 1] + check[i - 2]
print(check)