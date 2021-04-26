import sys
ln = sys.stdin.readline


# 0 1 2 3 4 5 6 7 8 9
# 6 2 5   4   6 3 7

# n 0~ 10 일때 답
ans_small_num = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]
lst = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

# max_val = ''
T = int(ln())
for t in range(T):
    n = int(ln())
    max_val = ''
    min_val = ''

    if n % 2 == 0:
        q = n // 2
        for i in range(q):
            max_val += '1'
    else:
        max_val = '7'
        q = (n - 3) // 2
        for i in range(q):
            max_val += '1'


    # print(max_val)




