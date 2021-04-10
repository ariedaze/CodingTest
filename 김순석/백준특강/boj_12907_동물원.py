import sys
ln = sys.stdin.readline

N = int(ln())
arr = list(map(int, ln().split()))
max_val = 2
check = [0] * 41

for i in arr:
    check[i] += 1

for i in check:
    if i > max_val:
        print(0)
        exit()
    max_val = i

a = check.count(2)
print(2 ** (a + (1 if 1 in check else 0)))
